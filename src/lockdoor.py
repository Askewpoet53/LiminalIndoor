import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)

time.sleep(1)

p = GPIO.PWM(14, 50)
time.sleep(1)
p.start(0)

p.ChangeDutyCycle(2)
p.ChangeDutyCycle(0)

p.stop()
GPIO.cleanup()


