# blink.py: Program to make the Raspberry Pi Pico 'blink'
# Contains helper functions to turn GPIO Pins High/Low
# Author: Timothy Do

import machine
import utime

def on(led):
    led.value(1)
    
def off(led):
    led.value(0)

def blink(led):
    on(led)
    utime.sleep(0.05)
    off(led)
    utime.sleep(0.05)




