import RPi.GPIO as GPIO


class lock(object):
    def __init__(self):
        GPIO.setMode(GPIO.BCM)
        # self.gpio = GPIO
        self.motorPin = 14


    def test(self):
        GPIO.setup(self.motorPin, GPIO.OUT)

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
        
        motor.stop()
        GPIO.cleanup()
