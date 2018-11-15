import sys


def main(argv):
    lock = argv[1]

    import time
    import RPi.GPIO as GPIO

    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    GPIO.setup(14, GPIO.OUT)

    p = GPIO.PWM(14, 50)

    p.start(0)

    if lock == "True":
        p.ChangeDutyCycle(7)
    else:
        p.ChangeDutyCycle(12)

    p.stop()

    GPIO.cleanup()


if __name__ == "__main__":
    if len(sys.argv) < 5:
        print("servo.py <lock?>")
    else:
        main(sys.argv)

