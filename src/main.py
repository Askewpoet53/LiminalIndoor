from flask import Flask, render_template, Response
import subprocess
import time
import picamera
import requests
from controllers.camera import camera

app = Flask(__name__)


@app.route("/doorbell/<door_id>")
def doorbell(door_id):
    print("Doorbell request...")
    with picamera.PiCamera() as camera:
        camera.resolution = (1024, 768)
        camera.start_preview()
        # Camera warm-up time
        time.sleep(2)
        camera.capture("img.jpg")
        print("...picture captured")

    file = open('img.jpg','rb')

    bytes = file.read()

    file.close()

    files = {'img': bytes}

    print("... creating request to backend ")

    print(files)
    # print(open('img.jpg','rb'))

    url = (
        "https://bffb941270be7a5179d6130698ccefd2.balena-devices.com/api/doorbell/"
        + door_id
        # "https://bffb941270be7a5179d6130698ccefd2.balena-devices.com/api/ping"
    )

    print(url)

    r = requests.post(url, data=files).content
    # r = requests.get(url).content

    print(r)

    return r


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

@app.route('/view/<door_id>')
def view(door_id):
    return render_template('index.html')

def gen(camera):
    """Video streaming generator function."""
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)

