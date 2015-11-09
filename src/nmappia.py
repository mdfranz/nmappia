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

        if self.config['inputs'].has_key('networks'):
            for n in self.config['inputs']['networks']:
                self.targets.append(n)
            
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
            time.sleep(30)
            print "Scan is %s percent complete" % self.engine.progress
        syslog.syslog("Completed scan")
if __name__ == "__main__":
    c = ConfigFile()
    c.generate_targets()
    se = ScanEngine(c)
    se.run()
