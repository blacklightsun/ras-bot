from machine import Pin
import time

led = Pin("LED", Pin.OUT)
pin7 = Pin(7, Pin.OUT)
pin8 = Pin(8, Pin.OUT)
pin9 = Pin(9, Pin.OUT)
pin10 = Pin(10, Pin.OUT)

led.on()
pin7.off()
pin8.off()
pin9.off()
pin10.off()
time.sleep(5)
led.off()
time.sleep(5)


led.on()
pin7.on()
time.sleep(5)
pin8.on()
time.sleep(5)
pin9.on()
time.sleep(5)
pin10.on()
time.sleep(5)
led.off()

led.on()
pin7.off()
pin8.off()
pin9.off()
pin10.off()
time.sleep(5)
led.off()
time.sleep(5)



