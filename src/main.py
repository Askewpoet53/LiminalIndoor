# import controllers.lock as lockScript
# import controllers.unlock as unlockScript
# import controllers.test as testScript

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
motorPin = 14
GPIO.setup(motorPin, GPIO.OUT)
# print(".. Motor setup...")
motor = GPIO.PWM(motorPin, 50)

from flask import Flask



app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello World!"


@app.route("/unlock")
def unlock():
    # unlockScript.run()
    motor.start(0)
    duty = 180 / 18 + 2
    motor.ChangeDutyCycle(duty)
    motor.stop()
    return "unlocking"


@app.route("/lock")
def lock():
    # lockScript.run()
    motor.start(0)
    duty = 90 / 18 + 2
    motor.ChangeDutyCycle(duty)
    motor.stop()
    return "locking"


@app.route("/test")
def test():
    # testScript.run()
    motor.start(0)
    motor.ChangeDutyCycle(5)
    motor.ChangeDutyCycle(0)
    motor.ChangeDutyCycle(10)
    motor.ChangeDutyCycle(5)
    motor.ChangeDutyCycle(0)
    motor.ChangeDutyCycle(10)
    motor.ChangeDutyCycle(5)
    motor.ChangeDutyCycle(0)
    motor.ChangeDutyCycle(10)
    motor.ChangeDutyCycle(5)
    motor.ChangeDutyCycle(0)
    motor.ChangeDutyCycle(10)
    motor.stop()
    return "testing"

@app.route("/ring")
def ring():
    return "ringing"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)

