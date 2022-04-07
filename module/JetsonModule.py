from config import gpioPins
from machine import Pin
from utime import sleep

def readDetection(pin):
    detection = Pin(pin, Pin.IN)
    return detection.value()

def changeState(option, pins):
    modeA = Pin(pins[0], Pin.OUT)
    modeA.value(0)
    modeB = Pin(pins[1], Pin.OUT)
    modeB.value(0)
    if (option == 1):
        modeA.value(1)
        modeB.value(0)
        sleep(2)
        modeA.value(0)
        modeB.value(0)
    elif (option == 2):
        modeA.value(0)
        modeB.value(1)
        sleep(2)
        modeA.value(0)
        modeB.value(0)
    else:
        modeA.value(0)
        modeB.value(0)
