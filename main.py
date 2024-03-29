# main.py: Driver Code for the Raspberry Pi Pico Temperature LED Project
# Author: Timothy Do
# Modifications:
# v1.0: Added Driving Code for 24/7 Led Temperature Checking at 75° F 7/14/21

import temp
import utime
import test

test.clean()
while(1):
    try:
        temp.tempLED(75)
        utime.sleep(10)
    except KeyboardInterrupt:
        break

print("Cleaning All GPIO Pins")
test.clean()
