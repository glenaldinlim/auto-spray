from machine import Pin

def MotorDriverControl(pins, states):
    out1 = Pin(pins[0], Pin.OUT)
    out2 = Pin(pins[1], Pin.OUT)
    
    out1.value(states[0])
    out2.value(states[1])
