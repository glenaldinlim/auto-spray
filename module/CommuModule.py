from machine import Pin
from utime import sleep
from config import gpioPins

output = Pin(gpioPins[1], Pin.IN)
modeA = Pin(gpioPins[2], Pin.OUT)
modeB = Pin(gpioPins[3], Pin.OUT)

def changeMode(mode, state):
    if(mode == 1):
        modeA.value(state)
        return state
    elif(mode == 2):
        modeB.value(state)
        return state
    else:
        modeA.value(0)
        modeB.value(0)
        return 0
    
def receiveDetection():
    return output.value()
