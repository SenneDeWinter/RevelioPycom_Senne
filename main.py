import pycom
import time
import lora
import sensor
import adafruitio
import wifi
import requests

sensor.uart_setup()

# lora.lora_join()
# while True:
#     distance = sensor.get_distance()
#     lora.lora_send(distance)
#     time.sleep(10)

wifi.wifi_connect()
while True:
    distance = sensor.get_distance()
    adafruitio.sendDataWifi(distance)
