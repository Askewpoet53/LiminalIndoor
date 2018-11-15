import sys
import time
import RPi.GPIO as GPIO


def main(argv):
	lock = argv[1]
	print(lock)

	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
	GPIO.setup(14, GPIO.OUT)

	p = GPIO.PWM(14, 50)

	p.start(0)

	if lock == "True":
		print("locking")
		p.ChangeDutyCycle(2)
	else:
		print("unlocking")
		p.ChangeDutyCycle(12)

	p.stop()
	GPIO.cleanup()


if __name__ == "__main__":
	if len(sys.argv) < 1:
		print("servo.py <lock?>")
	else:
		main(sys.argv)

