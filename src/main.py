from flask import Flask
import subprocess
import time
import picamera

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello World!"


@app.route("/doorbell")
def doorbell():

    with picamera.PiCamera() as camera:
        camera.resolution = (1024, 768)
        camera.start_preview()
        # Camera warm-up time
        time.sleep(2)
        camera.capture('peephole.jpg') 

    return"doorbell"

@app.route("/unlock")
def unlock():
    # unlockScript.run()
    subprocess.run("sudo python src/unlockdoor.py")
    return "unlocking"


@app.route("/lock")
def lock():
    # lockScript.run()
    subprocess.run("sudo python src/lockdoor.py")
    return "locking"


@app.route("/test")
def test():
    
    return "testing"

@app.route("/ring")
def ring():
    return "ringing"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)

