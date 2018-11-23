import sys
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)
p = GPIO.PWM(14, 50)
p.start(0)

p.ChangeDutyCycle(2)
p.ChangeDutyCycle(0)

p.stop()
GPIO.cleanup()


