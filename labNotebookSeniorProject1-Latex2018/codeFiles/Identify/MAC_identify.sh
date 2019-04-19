#!/bin/bash

sudo nmap -sn 192.168.1.0/24 | tee /home/bemoss/testing/test_scripts/MAC_out.txt
exit
