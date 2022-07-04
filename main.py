# Device Configuration
from config import pompPins, motorPins

# Built-in Module
from utime import sleep, time

# Third-party Module
from DHTModule import ReadValue
from MotorDriverModule import MotorDriverControl
from LimitSwitchModule import ReadSwitchValue
from CommuModule import changeMode, receiveDetection, readState
from APIModule import getDataAPI, postDataAPI
from WifiConnectionModule import WiFiConnection

# Initialize
print("[SYSTEM] Initialize")
print("[SYSTEM] Wifi Connection")
WiFiConnection()

print("[SYSTEM] Get Reset Queue Value and Store")
monitor = getDataAPI("/realtime/monitor")
resetQueue = monitor["data"]["reset"]
lastReset = (time() + 946707780) * 1000
monitor["data"].update({"reset": resetQueue+1})
monitor["data"].update({"lastReset": lastReset})
postDataAPI("/realtime/monitor", monitor["data"])

print("[SYSTEM] Starting System in 5 Second...")
sleep(5)

# Main Loop
while True:
    detect = 0
    MotorDriverControl(motorPins[:2], [0, 0])
    MotorDriverControl(pompPins[:2], [0, 0])
    print("[STAT] Standby")
    if (readState() == 1):
        config = getDataAPI("/realtime/config")
        mode = config["data"]["mode"]
        changeMode(mode,1)
        sleep(2)
        MotorDriverControl(motorPins[:2], [1, 0])
        while(readState() == 1):
            if(receiveDetection() == 1):
                detect+=1
                MotorDriverControl(pompPins[:2], [1, 0])
                sleep(1)
            else:
                MotorDriverControl(pompPins[:2], [0, 0])
                sleep(1)
            if(ReadSwitchValue(1) == 1):
                MotorDriverControl(motorPins[:2], [0, 0])
                changeMode(3,0)
            elif(ReadSwitchValue(2) == 1):
                MotorDriverControl(motorPins[:2], [0, 0])
                sleep(3)
                MotorDriverControl(motorPins[:2], [0, 1])
        record = {'detection_result': detect, 'mode': mode}
        postDataAPI("/firestore/records", record)
