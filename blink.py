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

def square(speaker,freq,duration):
    for i in range(round(duration*freq/2)):
        on(speaker)
        utime.sleep(1/freq)
        off(speaker)
        utime.sleep(1/freq)
        
if __name__ ==  '__main__':
    speaker = machine.Pin(16,machine.Pin.OUT)
    square(speaker,500,10)
    



