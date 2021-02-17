import pycom
from network import WLAN
import machine
wlan = WLAN(mode=WLAN.STA)
pycom.heartbeat(False)

wlan.connect(ssid='UniFi-2.4GHz', auth=(WLAN.WPA2, '??'))
while not wlan.isconnected():
    print("Not yet connected")
    pycom.rgbled(0xFF0000)
print("WiFi connected succesfully")
pycom.rgbled(0x00FF00)
print(wlan.ifconfig())
