from network import WLAN
import machine
import requests
wlan = WLAN(mode=WLAN.STA)

def wifi_connect():
    wlan.connect(ssid='IoT', auth=(WLAN.WPA2, 'KdGIoT92!'))
    while not wlan.isconnected():
        print("WiFi: Not yet connected")
print("WiFi: connected succesfully")
print(wlan.ifconfig())
