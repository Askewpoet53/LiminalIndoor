import controllers.lock as lock
import controllers.unlock as unlock

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello World!"


@app.route("/unlock")
def unlock():
    unlock.run()
    return "unlocking"


@app.route("/lock")
def lock():
    lock.run()
    return "locking"


@app.route("/ring")
def ring():
    return "ringing"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)

