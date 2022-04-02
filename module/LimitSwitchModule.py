from machine import Pin
from config import limitSwitchPins

swFront = Pin(limitSwitchPins[0], Pin.IN)
swRear = Pin(limitSwitchPins[1], Pin.IN)

def ReadSwitchValue(option):
    if option == 1:
        return swFront.value()
    elif option == 2:
        return swRear.value()
    else:
        return 0
