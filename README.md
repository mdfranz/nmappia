# Nmappia - a port scanning aqueduct

# Purpose
Channel various inputs of targets to nmap and then distribute them out outputs for indexing or notification of changes.

## Inputs

Targets can be selected from one our mor inputs:
- Netblock Lists
- Arbitrary File Lists
- Compute APIs (EC2)
- DNS APIs (Linode, Route53, Zone Transfers)

## Outputs
After scans complete the outputs can be sent to the following
- Pure Syslog output
- Elasticsearch
- JSON Dumps
- JSON TCP Stream (suitable for sending to NXLOG)
- Slack Channels
- PagerDuty Alerts

# Configuration

Inputs and Outputs and Scan options are configured in nmappia.conf



# External Dependencies
 - python-libnmap
 - boto
 - Nmap 

# Installation

A simple Ansible playbook will be provided to install and configure on local or remote hosts.

# What about the Name

There were already too many projects with the name aqueduct so I was looking at the names of Roman acqueducts and I ran accross Aqua Appia
 - http://www.crystalinks.com/romeaqueducts.html
 - https://en.wikipedia.org/wiki/Aqueduct_(water_supply)
