#!/usr/bin/env python

DEBUG=True

import json

class ConfigFile(object):
    def __init__(self,f="nmappia.conf"):
        self.debug = True
        self.tmpdir = "/tmp"
        with open(f) as config_file:
            self.config = json.load(config_file)

            if self.debug:
                print `self.config`

    def make_command(self):
        """Form nmap command string"""
        command = " %s " % (self.config['policy']['scan_options'])

if __name__ == "__main__":
    c = ConfigFile()
