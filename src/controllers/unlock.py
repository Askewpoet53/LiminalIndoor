import RPi.GPIO as GPIO
from time import sleep


def run():
    GPIO.setmode(GPIO.BCM)
    motorPin = 14
    GPIO.setup(motorPin, GPIO.OUT)
    # print(".. Motor setup...")
    motor = GPIO.PWM(motorPin, 50)
    duty = 0 / 18 + 2
  
    motor.ChangeDutyCycle(duty)
    motor.ChangeDutyCycle(0)
    sleep(1)
    GPIO.cleanup()
