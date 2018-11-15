import controllers.lock as lockScript
import controllers.unlock as unlockScript

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello World!"


@app.route("/unlock")
def unlock():
    unlockScript.run()
    return "unlocking"


@app.route("/lock")
def lock():
    lockScript.run()
    return "locking"


@app.route("/ring")
def ring():
    return "ringing"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)

