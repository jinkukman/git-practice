from machine import Pin
import time

led1 = Pin(15, Pin.OUT)

while True :
    led1.value(1)
    time.sleep(1,0)
    led1.value(0)
    time.sleep(1,0)