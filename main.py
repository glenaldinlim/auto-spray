# Device Configuration
from config import pompPins, motorPins

# Built-in Module
import json
from utime import sleep

# Third-party Module
from DHTModule import ReadValue
from MotorDriverModule import MotorDriverControl
from LimitSwitchModule import ReadSwitchValue
# from WifiManagerModule import openWifiManager
from CommuModule import changeMode, receiveDetection
from APIModule import getDataAPI, postDataAPI
from FirebaseModule import getData, storeData, putData, deleteData
from WiFiConnectionModule import WiFiConnection

# Initialize
print("Initialize System...")
# openWifiManager()
WiFiConnection()
resetQueue = getData("/monitor")
print(resetQueue)
print("Starting System in 5 Second...")
sleep(5)

# Main Loop
# while True:
#     print("--------------------")
#     print(changeMode(1,1))
#     print(receiveDetection())
#     print("--------------------")
#     sleep(2)
#     MotorDriverControl(motorPins[:2], [1, 0])
#     MotorDriverControl(pompPins[:2], [1,0])
#     sleep(3.2)
#     MotorDriverControl(motorPins[:2], [0, 0])
#     MotorDriverControl(pompPins[:2], [0,0])
#     sleep(2)
#     MotorDriverControl(motorPins[:2], [0, 1])
#     sleep(3.2)
#     MotorDriverControl(motorPins[:2], [0, 0])
#     sleep(2)
#     print(ReadSwitchValue(1))
#     print(ReadSwitchValue(2))
#     print(ReadSwitchValue(0))
#     sleep(5)
#     if(ReadSwitchValue(1) == 1):
#         MotorDriverControl(motorPins[:2], [0, 0])
#     elif(ReadSwitchValue(2) == 1):
#         MotorDriverControl(motorPins[:2], [0, 0])
#     else:
#         print("Fck")
#         MotorDriverControl(motorPins[:2], [1, 0])

