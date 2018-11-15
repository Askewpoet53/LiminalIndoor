


def run():
    GPIO.setmode(GPIO.BCM)
    motorPin = 14
    GPIO.setup(motorPin, GPIO.OUT)
    # print(".. Motor setup...")
    motor = GPIO.PWM(motorPin, 50)
    # GPIO.output(motorPin, True)
    duty = 90 / 18 + 2

    motor.start(0)

    motor.ChangeDutyCycle(duty)
    # sleep(2)
    motor.ChangeDutyCycle(0)
    # GPIO.output(motorPin, False)
    sleep(2)
    motor.stop()
    GPIO.cleanup()
