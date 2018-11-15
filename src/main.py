from flask import Flask
import RPi.GPIO as GPIO

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello World!"


@app.route("/testServo")
def testServo():
    print("testing servo...")
    GPIO.setmode(GPIO.BOARD)
    motorPin = 14
    GPIO.setup(motorPin, GPIO.OUT)
    motor = GPIO.PWM(motorPin, 50)
    motor.start(0)  # Initialization
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
    return "testing"


@app.route("/unlock")
def unlock():
    return "unlocking"


@app.route("/ring")
def ring():
    return "ringing"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)

