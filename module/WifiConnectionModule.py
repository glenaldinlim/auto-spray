import network
from utime import sleep
from config import wifi_ssid, wifi_password

def WiFiConnection():
    wifi = network.WLAN(network.STA_IF)
    wifi.active(True)
    print("Connecting to {} network".format(wifi_ssid), end="")
    while not wifi.isconnected():
        wifi.connect(wifi_ssid, wifi_password)
        print(".", end="")
        sleep(1)
    print("\nSuccess to connect with {} network!".format(wifi_ssid))
    config = wifi.ifconfig()
    print("Device IP: {}".format(config[0]))
