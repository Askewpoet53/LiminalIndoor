import RPi.GPIO as GPIO
from time import sleep

def run():
    GPIO.setmode(GPIO.BCM)
    motorPin = 14
    GPIO.setup(motorPin, GPIO.OUT)
    # print(".. Motor setup...")
    motor = GPIO.PWM(motorPin, 50)
    duty = 90 / 18 + 2
    GPIO.output(motorPin, True)
    motor.ChangeDutyCycle(duty)
    sleep(1)
    GPIO.output(motorPin, False)
    GPIO.cleanup()
