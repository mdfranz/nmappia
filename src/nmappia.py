#!/usr/bin/env python

import json,syslog,time

from libnmap.parser import NmapParser
from libnmap.process import NmapProcess


class ConfigFile(object):
    def __init__(self,f="nmappia.conf",debug=True):
        self.targets = []
        self.debug = debug
        self.options = ""
        with open(f) as config_file:
            self.config = json.load(config_file)

            if self.debug:
                print "=== Configuration ==="
                print `self.config`

    def generate_targets(self):
        syslog.syslog("Starting target generation")

        # Read from multiple targets sources
        if self.config['inputs'].has_key('networks'):
            for n in self.config['inputs']['networks']:
                self.targets.append(n)
        if self.config['inputs'].has_key('file'):
            with open(self.config['inputs']['file']) as f:
                for l in f:
                    self.targets.append(l)
            
        if self.debug:
            print "=== Targets ==="
            print `self.targets`
        
        syslog.syslog("Completed target generation")

    def form_command(self):
        """Form nmap command string"""
        self.options = " %s " % (self.config['policy']['scan_options'])

class ScanEngine(object):
    def __init__(self,config):
        self.engine = NmapProcess(config.targets, config.options)

    def run(self):
        """Execute scan"""
        syslog.syslog("Starting scan")
        self.engine.run_background()
        while self.engine.is_running():
            time.sleep(15)
            print "Scan is %s percent complete" % self.engine.progress
        syslog.syslog("Completed scan")
    
    def process(self):
        """parse and pre-process scan results"""
        
        try:
            self.parsed = NmapParser.parse(self.engine.stdout)
            syslog.syslog("Processing output")
        except Exception as e:
            syslog.syslog("Failed to parse output"+e)

        for h in self.parsed.hosts:
            print h.address
            
if __name__ == "__main__":
    sc = ConfigFile()
    sc.generate_targets()
    se = ScanEngine(sc)
    se.run()
    se.process()
    
