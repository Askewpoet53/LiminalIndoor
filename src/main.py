from flask import Flask
import os
from subprocess import Popen


app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello World!"


@app.route("/unlock")
def unlock():
    # unlockScript.run()
    devnull = open(os.devnull, 'wb') # in python < 3.3
    Popen(['nohup', 'src/unlockdoor.py'], stdout=devnull, stderr=devnull)
    return "unlocking"


@app.route("/lock")
def lock():
    # lockScript.run()
    devnull = open(os.devnull, 'wb') # in python < 3.3
    Popen(['nohup', 'src/lockdoor.py'], stdout=devnull, stderr=devnull)
    
    return "locking"


@app.route("/test")
def test():
    
    return "testing"

@app.route("/ring")
def ring():
    return "ringing"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)

