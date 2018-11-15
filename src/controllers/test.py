import RPi.GPIO as GPIO
from time import sleep


def run():
    GPIO.setmode(GPIO.BCM)
    motorPin = 14
    GPIO.setup(motorPin, GPIO.OUT)
    # print(".. Motor setup...")
    motor = GPIO.PWM(motorPin, 50)
    GPIO.output(motorPin, True)

    motor.start(0)

    motor.ChangeDutyCycle(5)
    motor.ChangeDutyCycle(0)
    motor.ChangeDutyCycle(10)
    motor.ChangeDutyCycle(0)
    motor.ChangeDutyCycle(5)
    motor.ChangeDutyCycle(0)
    motor.ChangeDutyCycle(10)
    motor.ChangeDutyCycle(0)
    motor.ChangeDutyCycle(5)
    motor.ChangeDutyCycle(0)
    motor.ChangeDutyCycle(10)
    motor.ChangeDutyCycle(0)
    GPIO.output(motorPin, False)
    sleep(2)
    GPIO.cleanup()
