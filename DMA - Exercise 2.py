
'''
============================================================================
 Name         : DMA - Exercise 2
 Author       : Zayed AlTamimi (ZKA224)
 Version      : 1
 Date Modified: 15 Sept. 2024
 Description  : RGB Story - The Invention of TVs
============================================================================
 Sources:
 https://learn.adafruit.com/adafruit-feather-m4-express-atsamd51/circuitpython-internal-rgb-led
 - Was used in the initialization to define the libraries, find the correct Pin Name, and create the LED object.
 - Also, to create the endless transition of various colors in the Fourth LED stage
============================================================================
'''

"""CircuitPython Essentials Internal RGB LED red, green, blue example"""
import time
import board
from rainbowio import colorwheel

#Indicate that the code is Running
print("Starting Up...")

#Check what board will be used to ensure the correct pin name of the neopixel is used.
#Will also create the LED object;
if hasattr(board, "APA102_SCK"):
    import adafruit_dotstar
    led = adafruit_dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1)
else:
    import neopixel
    led = neopixel.NeoPixel(board.NEOPIXEL, 1)

#Set the brightness to be halfway, the maximum brightness is at 1
led.brightness = 0.5

#Initiate variables that will be updated throughout the code execution
ctr = 0 #Represents the number of iterations or cycles of the LED for the second and third sections of the LED display.
speed = 0.3 #Will be used to increase the frequency of LED colors switching between white and black or off

#First LED Stage 'The research before inventing the first Black and White TV'
#Will make the RGB start blinking a white color by switching between displaying a white color and turning off, the frequency of switching will slowly increase
#The process will continue until the frequency of blinking cannot be faster anymore. In other words, when the speed cannot be reduced any further.
while (speed > 0):
    led[0] = (5, 5, 5)
    led[0] = (0, 0, 0)
    time.sleep(speed)
    speed -= 0.01


ctr = 0
#Second LED Stage 'The invention of Black and White TVs'
#Will make the RGB alternate between white and turning off, but this time there will be no blinking but instead it will alternate between both options 5 times
while (ctr < 5):
    led.brightness = 0.2
    led[0] = (80, 70, 70)
    time.sleep(0.25)
    led[0] = (0, 0, 0)
    time.sleep(0.5)
    ctr += 1


ctr = 0
#Third LED Stage 'The introduction of colors to TVs'
#Will make the RGB go through 3 different phases/patterns. This stage is also when new colors aside from white will be displayed.
#It will start by alternating between a Red Color and Off five times. Then, it will alternate between Red and Green five times, and finally between Red, Green, and Blue (or RGB) five times.
while (ctr < 15):
    #Will start with blinking the Red Color 5 times
    if (ctr < 5):
        led[0] = (255, 0, 0)
        time.sleep(0.25)
        led[0] = (0, 0, 0)
        time.sleep(0.5)
        ctr += 1

    #Will alternate between Red and Green Colors 5 times
    elif (ctr < 10):
        led[0] = (255, 0, 0)
        time.sleep(0.25)
        led[0] = (0, 255, 0)
        time.sleep(0.5)
        ctr += 1

    #Will alternate between Red, Green, and Blue Colors, 5 times
    else:
        led[0] = (255, 0, 0)
        time.sleep(0.25)
        led[0] = (0, 255, 0)
        time.sleep(0.25)
        led[0] = (0, 0, 255)
        time.sleep(0.5)
        ctr += 1

#Fourth LED Stage 'The Current TV Stage where TVs can display over a Billion Colors'
#Will Cycle Through an RGB Rainbow.
i = 0 #Start at the Beginning of the Rainbow
ctr = 0
while ctr < 2000:
    i = (i+1) % 256
    led.fill(colorwheel(i))
    time.sleep(0.0001)
    ctr += 1
 
