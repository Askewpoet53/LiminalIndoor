from picamera import PiCamera
import datetime


class camera_control(object):
    def __init__(self):
        self.camera = PiCamera()
        self.camera.resolution = (1024, 768)
        self.camera.start_preview()

    def snap(self, callback):
        self.camera.capture("img.jpg")
        print(datetime.datetime.now())
        callback("stuff")

