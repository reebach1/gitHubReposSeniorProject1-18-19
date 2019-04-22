#!/bin/bash

sshpass -p "BradleyEE" ssh -o StrictHostKeyChecking=no pi@192.168.1.41 "python /home/pi/testing_scripts/XBEETEST.py" 

