# Nmappia - a port scanning aqueduct

# Purpose
Channel various inputs of targets to nmap and then distribute them out outputs for indexing or action

## Inputs

Targets can be selected from one our mor inputs:
- Network Lists
- DNS APIs (Linode, Route53, Zone Transfers)
- Compute APIs (
- Arbitrary

After scans complete the outputs can be sent to the following
- Pure Syslog output
- JSON TCP Stream (suitable for sending to NXLOG)
- JSON Files
- SQS
- Elasticsearch

# What about the Name

There were already too many projects with the name aqueduct so I was looking at the names of Roman acqueducts and I ran accross Aqua Appia

 - http://www.crystalinks.com/romeaqueducts.html
 
