from config import dhtPin
from machine import Pin
import dht

def ReadValue(option):
    try:
        d = dht.DHT22(Pin(dhtPin))
        d.measure()
        if option == 1:
            return d.temperature()
        elif option == 2:
            return d.humidity()
        else:
            return 0
    except OSError as err:
        if err.args[0] == 116:
            return 0.1
        else:
            return 0.2
