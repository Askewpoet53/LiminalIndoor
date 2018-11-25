from flask import Flask
import subprocess
import time
import pyaudio
import wave
import picamera
import requests

app = Flask(__name__)

API_LINK = "https://bffb941270be7a5179d6130698ccefd2.balena-devices.com/api/"


@app.route("/doorbell/<string:door_id>")
def doorbell(door_id):
    with picamera.PiCamera() as camera:
        camera.resolution = (1024, 768)
        camera.start_preview()
        # Camera warm-up time
        time.sleep(2)
        camera.capture("peephole.jpg")

    peephole_img = open("peephole.jpg")

    data = {"img": peephole_img}
    
    r = requests.post(API_LINK + "doorbell/" + door_id, data=data)
    
    response = r.json()

    return response.data


@app.route("/pin/<string:door_id>")
def pin(door_id):
    with picamera.PiCamera() as camera:
        camera.resolution = (1024, 768)
        camera.start_preview()
        # Camera warm-up time
        time.sleep(2)
        camera.capture("peephole.jpg")

    peephole_img = open("peephole.jpg")

    data = {"img": peephole_img}

    r = requests.post(API_LINK + "pin/" + door_id, data=data)

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


def bell():
    CHUNK = 1024
    wf = wave.open('ring.wav', "rb")
    # instantiate PyAudio (1)
    p = pyaudio.PyAudio()

    # open stream (2)
    stream = p.open(
        format=p.get_format_from_width(wf.getsampwidth()),
        channels=wf.getnchannels(),
        rate=wf.getframerate(),
        output=True,
    )

    # read data
    data = wf.readframes(CHUNK)

    # play stream (3)
    while len(data) > 0:
        stream.write(data)
        data = wf.readframes(CHUNK)

    # stop stream (4)
    stream.stop_stream()
    stream.close()
