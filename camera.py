import picamera
from subprocess import call
import picamera
from datetime import datetime, timezone
from time import sleep
import pytz

def takepicture():
    completeFilePath = "/home/pi/pi-camera-stream-flask/static/newimage.jpg"
    print("About to take a picture.")
    with picamera.PiCamera() as camera:
        currentTime = datetime.now(timezone.utc).astimezone(pytz.timezone('US/Pacific'))
        camera.resolution = (1280,720)
        camera.capture("/home/pi/pi-camera-stream-flask/static/newimage.jpg")
        print("Picture taken.")
        print("About to timestamp picture")
        timestampMessage = currentTime.strftime("%Y.%m.%d - %H:%M:%S")
        cmd = "/usr/bin/convert " + completeFilePath + " -pointsize 32 \
            -fill red -annotate +700+500 '" + timestampMessage + "' " + completeFilePath
        call([cmd], shell=True)
        print("Timestamped picture")