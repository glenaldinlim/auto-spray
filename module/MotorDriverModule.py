from machine import Pin, PWM

def MotorDriverControl(pins, states, pwm_duty = 1023):
    out1 = Pin(pins[0], Pin.OUT)
    out2 = Pin(pins[1], Pin.OUT)
    enab = PWM(Pin(pins[2]))
    
    out1.value(states[0])
    out2.value(states[1])
    enab.duty(pwm_duty)
