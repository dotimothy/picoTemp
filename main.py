# main.py: Driver Code for the Raspberry Pi Pico Temperature LED Project
# Author: Timothy Do
# Modifications:
# v1.0: Added Driving Code for 24/7 Led Temperature Checking at 100° F 7/14/21

import temp
import utime

while(1):
    temp.tempLED(100)
    utime.sleep(10)
    
