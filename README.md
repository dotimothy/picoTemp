# picoTemp
## An LED Temperature Indicator Using the Raspberry Pi Pico
<img src="picoTemp.gif"/> 
<img width="75%" src="https://www.raspberrypi.com/documentation/microcontrollers/images/pico-pinout.svg">
To Start, Please Connect the Follow '+' Component Leads to the Following GPIO/Power Pins/, as shown in the Pico Pinout: <br><br>
Green LED -> GPIO Pin 0 (Physical 1)<br>
Red LED -> GPIO Pin 15 (Physical 20)<br>
DC Buzzer -> GPIO Pin 13 (Physical 17)<br><br>

All the negative leads of the above components will go to ground (GND). <br>

There is a specific configuration for the fan to allow more output current via a relay: <br>
Fan Relay 'In' -> GPIO Pin 3 (Physical 5)<br>
Fan Relay DC '+' -> 3.3V V_Out (Physical 36) <br>
Fan Relay DC '-' -> GND <br>
Fan Relay 'NC' -> GND <br>
Fan Relay 'NO' -> 5V V_bus (Physical 40) <Br>
Fan '+' -> Fan Relay 'COM'
Fan '-' -> GND

The Other Python Files are use to assist main.py & some debugging tests.

When the **Green** Led Turns On, that means the temperature is **below** the threshold temperature, Red Otherwise. The other components will activate when the temperature is above the threshold
<br></br> 
<img src="console.PNG">
## Things to Work On / Improve
1. Design of the Chassis should be More Portable & Sustainable
2. Thersehold should be adjusted manually by the user (e.g. adding a potentiometer)
3. Temperature could be displayed to the user (requires external display)

This is A Good Starting Project for Learning the Raspberry Pi Pico!

Note: There is a Hard Coded Temperature Threshold of 80° F

A Fan was placed in the Schematic to Cool the CPU to produce the most accurate comparison with Ambient Air Temperature.
 
