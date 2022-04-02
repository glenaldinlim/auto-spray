import wifimgr

try:
  import usocket as socket
except:
  import socket

def openWifiManager():
    wlan = wifimgr.get_connection()
    if wlan is None:
        print("Could not initialize the network connection.")
        while True:
            pass
