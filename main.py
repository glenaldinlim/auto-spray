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
from CommuModule import changeMode, receiveDetection, readState
from APIModule import getDataAPI, postDataAPI
from FirebaseModule import getData, storeData, putData, deleteData
from WifiConnectionModule import WiFiConnection

# Initialize
print("[SYSTEM] Initialize")
print("[SYSTEM] Wifi Connection")
# openWifiManager()
WiFiConnection()

print("[SYSTEM] Get Reset Queue Value and Store")
monitor = getDataAPI("/realtime/monitor")
resetQueue = monitor["data"]["reset"]

print("Starting System in 5 Second...")
sleep(5)

detect = 0

# Main Loop
while True:
    print("Change to Mode 1")
    changeMode(1,1)
    sleep(2)
    changeMode(3,0)
    sleep(2)
    while (readState() == 0):
        if readState() == 1:
            pass
    config = getDataAPI("/realtime/config")
    modeJetson = config["data"]["mode"]
    changeMode(modeJetson,1)
    sleep(2)
    changeMode(3,0)
    sleep(2)
    detect = 0
    while (readState() == 0):
        if readState() == 1:
            pass
    while(readState() == 1):
        if(ReadSwitchValue(1) == 1):
            MotorDriverControl(motorPins[:2], [0, 0])
            sleep(3)
            MotorDriverControl(motorPins[:2], [0, 1])
        elif(ReadSwitchValue(2) == 1):
            MotorDriverControl(motorPins[:2], [0, 0])
            sleep(3)
            MotorDriverControl(motorPins[:2], [0, 1])
        else:
            MotorDriverControl(motorPins[:2], [1, 0])
        if(receiveDetection() == 1):
            detect+=1
            MotorDriverControl(motorPins[:2], [1, 0])
            sleep(3)
            MotorDriverControl(motorPins[:2], [1, 0])
    print(detect)
    break
