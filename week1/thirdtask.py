import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(26,GPIO.OUT)
GPIO.setup(21,GPIO.IN)
if GPIO.input(21)==1:
    GPIO.output(26,1)
else:
    GPIO.output(26,0)