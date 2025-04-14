import RPi.GPIO as gpio
leds = [2,3,4,17,27,22,10,9]
aux = [21,20,26,16,19,25,23,24]
gpio.setmode(gpio.BCM)
gpio.setup(leds,gpio.OUT)
gpio.setup(aux,gpio.IN)
while True:
    for i in range(8):
        value = gpio.input(aux[i])
        gpio.output(leds[i],value)