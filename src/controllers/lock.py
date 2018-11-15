import RPi.GPIO as GPIO


class lock(object):
    def __init__(self):
        print("creating lock class...")
        try:
            GPIO.setmode(GPIO.BCM)
        except RuntimeError:
            print("error")
        # self.gpio = GPIO
        self.motorPin = 14
        print(GPIO.getmode())

    def test(self):
        print("... in lock.test()")
        GPIO.setup(self.motorPin, GPIO.OUT)
        print(".. Motor setup...")

        motor = GPIO.PWM(self.motorPin, 50)

        motor.start(2.5)  # Initialization

        motor.ChangeDutyCycle(5)
        motor.ChangeDutyCycle(7.5)
        motor.ChangeDutyCycle(10)
        motor.ChangeDutyCycle(12.5)
        motor.ChangeDutyCycle(10)
        motor.ChangeDutyCycle(7.5)
        motor.ChangeDutyCycle(5)
        motor.ChangeDutyCycle(2.5)

        print("...Cleaning Resources")
        motor.stop()
        GPIO.cleanup()