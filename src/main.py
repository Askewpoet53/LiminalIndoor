from flask import Flask
import subprocess
import time
import picamera
import requests

app = Flask(__name__)


@app.route("/doorbell/<door_id>")
def doorbell(door_id):
    print("Doorbell request...")
    with picamera.PiCamera() as camera:
        camera.resolution = (1024, 768)
        camera.start_preview()
        # Camera warm-up time
        time.sleep(2)
        camera.capture("peephole.jpg")
        print("...picture captured")

    peephole_img = open("peephole.jpg", "rb")

    data = {"img": peephole_img}
    print(peephole_img)
    print("... creating request to backend ")

    url = (
        # "https://bffb941270be7a5179d6130698ccefd2.balena-devices.com/api/doorbell/"
        # + door_id
        "https://bffb941270be7a5179d6130698ccefd2.balena-devices.com/api/ping"
    )

    # r = requests.post(url, files=data)
    r = requests.get(url)

    print(r.status_code + " " + r.json())

    # print(r.json())

    return "testing"


@app.route("/pin/<door_id>")
def pin(door_id):
    with picamera.PiCamera() as camera:
        camera.resolution = (1024, 768)
        camera.start_preview()
        # Camera warm-up time
        time.sleep(2)
        camera.capture("peephole.jpg")

    peephole_img = open("peephole.jpg")

    data = {"img": peephole_img}

    r = requests.post(
        "https://bffb941270be7a5179d6130698ccefd2.balena-devices.com/api"
        + "pin/"
        + door_id,
        data=data,
    )

    response = r.json()
    if response.validated:
        # call unlock script
        print("user validated")
    else:
        # call lock script
        print("user not validated")

    return response.message


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)

