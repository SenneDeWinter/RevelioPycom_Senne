from network import LoRa
import socket
import time
import ubinascii
import ustruct


lora = LoRa(mode=LoRa.LORAWAN, region=LoRa.EU868)
app_eui = ubinascii.unhexlify('70B3D57ED003E4C2')
app_key = ubinascii.unhexlify('DCDC3BE9EBEF084FCE04EDF06DB6EFED')

def lora_join():
    lora.join(activation=LoRa.OTAA, auth=(app_eui, app_key), timeout=0)
    while not lora.has_joined():
        time.sleep(2.5)
        print('LoRa: Not yet joined...')
    print("LoRa: Joined")

def lora_send(data):
    s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
    s.setsockopt(socket.SOL_LORA, socket.SO_DR, 5)
    s.setblocking(True)
    packet = ustruct.pack('f', data)
    s.send(packet)
