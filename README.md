# Nmappia - a port scanning aqueduct

# Purpose
Channel various inputs of targets to nmap and then distribute them out outputs for indexing or action

## Inputs

Targets can be selected from one our mor inputs:
- Network Lists
- DNS APIs (Linode, Route53, Zone Transfers)
- Compute APIs (
- Arbitrary


## Outputs
After scans complete the outputs can be sent to the following
- Pure Syslog output
- JSON TCP Stream (suitable for sending to NXLOG)
- JSON Files
- SQS
- Elasticsearch

# Configuration

# Installation

A simple Ansible playbook will be provided to install and configure on local or remote hosts.



# What about the Name

There were already too many projects with the name aqueduct so I was looking at the names of Roman acqueducts and I ran accross Aqua Appia

 - http://www.crystalinks.com/romeaqueducts.html
 
