from flask import Flask
import subprocess

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello World!"


@app.route("/unlock")
def unlock():
    # unlockScript.run()
    subprocess.run("python src/servo.py True")
    return "unlocking"


@app.route("/lock")
def lock():
    # lockScript.run()
    subprocess.run("python src/servo.py False")
    return "locking"


@app.route("/test")
def test():
    
    return "testing"

@app.route("/ring")
def ring():
    return "ringing"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)

