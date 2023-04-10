# temp.py: Measuring Temperature of Raspberry Pi Pico Sensor
# Author: Timothy Do
# Modifications:
# v1.0: Added Helper Voltage Functions, converting ADC to Temperatures (7/7/21)
# v1.1: Made Threshold Voltage a parameter rather than input (7/14/21)
# v1.2: Added a speaker output to alert the user of high temperature (4/10/2023)


import machine
import utime
import blink
import test

#Global Variables
sense = machine.ADC(4)
factor = 3.3 /  65535
red = machine.Pin(15,machine.Pin.OUT)
speaker = machine.Pin(13,machine.Pin.OUT)
green = machine.Pin(0,machine.Pin.OUT)

#Voltage Conversions Specific to Sensor
def voltToCel(voltage):
    return 27 - (voltage - 0.706)/0.001721

def voltToFar(voltage):
    return (voltToCel(voltage) * (9/5)) + 32

def voltToKel(voltage):
    return voltToCel(voltage) + 273.15

def tempLED(limit):
    blink.off(red)
    blink.off(green)
    loop = 0
    while(loop <= 100):
        loop = loop + 1
        volt = sense.read_u16() * factor
        print(str(loop) + ". Temp on Pico: \n" + str(voltToFar(volt)) + "° F\n" + str(voltToCel(volt)) + "° C\n" + str(voltToKel(volt)) + "° K\n")
        if(voltToFar(volt) >= limit):
            print("Too Hot!\n")
            blink.on(red)
            blink.square(speaker,500,1)
            blink.off(green)
        else:
            print("Good!\n")
            blink.on(green)
            blink.off(red)
        utime.sleep(1)
    blink.off(red)
    blink.off(green)
    test.clean()
    print("Done")
    
def main():
    limit = float(input("Threshold Temp in F: "))
    tempLED(limit)



