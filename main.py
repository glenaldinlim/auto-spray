# Device Configuration
from config import pompPins, motorPins

# Built-in Module
import json
from utime import sleep

# Third-party Module
from DHTModule import ReadValue
from MotorDriverModule import MotorDriverControl
from LimitSwitchModule import ReadSwitchValue
from WifiManagerModule import openWifiManager

# Initialize
print("Initialize System...")
# openWifiManager()
print("Starting System in 5 Second...")
sleep(5)

# Main Loop
while True:
    if(ReadSwitchValue(1) == 1):
        MotorDriverControl(motorPins[:2], [1, 0])
    elif(ReadSwitchValue(2) == 1):
        MotorDriverControl(motorPins[:2], [1, 0])
    else:
        MotorDriverControl(motorPins[:2], [0, 0])

