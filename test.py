import machine
import time
# test.py: Debugging Modules for the Raspberry Pi Pico
# Author: Timothy Do

import blink

def check(duration):
    for i in range(29):
        print("Testing Pin " + str(i))
        led = machine.Pin(i,machine.Pin.OUT)
        blink.on(led)
        time.sleep(duration)
        blink.off(led)
        time.sleep(duration)

def onBoard():
    led = machine.Pin(25,machine.Pin.OUT)
    for i in range(20):
        blink.blink(led)
    print("On Board Test Done")
    
def clean():
    for i in range(29):
        print("Cleaning up GPIO Pin " + str(i))
        led = machine.Pin(i,machine.Pin.OUT)
        blink.off(led)


