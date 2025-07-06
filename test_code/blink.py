from machine import Pin, Timer

led1 = Pin(15, Pin.OUT)
led2 = Pin("LED", Pin.OUT)

LED_state = True
tim = Timer()

def tick(timer):
    global led1, led2, LED_state
    print(timer)
    LED_state = not LED_state
    led1.value(LED_state)
    led2.value(not LED_state)
    
tim.init(freq=3, mode=Timer.PERIODIC, callback=tick)