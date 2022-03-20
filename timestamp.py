from subprocess import call
import picamera
from datetime import datetime, timezone
from time import sleep
import pytz

filePath = "/home/pi/home-sec/timestamped-pics/"
picTotal = 5
picCount = 0

while picCount < picTotal:
    currentTime = datetime.now(timezone.utc).astimezone(pytz.timezone('US/Pacific'))
    picTime = currentTime.strftime("%Y.%m.%d-%H%M%S")
    picName = picTime + '.jpg'
    completeFilePath = filePath + picName

    print("About to take a picture.")
    with picamera.PiCamera() as camera:
        camera.resolution = (1280,720)
        camera.capture(completeFilePath)
    print("Picture taken.")

    print("About to timestamp picture")
    timestampMessage = currentTime.strftime("%Y.%m.%d - %H:%M:%S")
    cmd = "/usr/bin/convert " + completeFilePath + " -pointsize 32 \
        -fill red -annotate +700+500 '" + timestampMessage + "' " + completeFilePath
    call([cmd], shell=True)
    print("Timestamped picture")

    picCount += 1
    sleep(5)
