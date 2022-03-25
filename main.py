from time import sleep
from blob_storage import BlobStorage
from mail import send_mail
import picam
import camera
import datetime

blobStorage = BlobStorage()
motionState = False
lastCheckedTime = datetime.datetime.now()
shouldRunMotionDetection = True
while True:
    currentDate = datetime.datetime.now()
    if currentDate.second >= 58 and currentDate.second <= 60:
        if lastCheckedTime < currentDate:
            shouldRunMotionDetection = True if (blobStorage.GetStatus() == "on") else False
            sleep(2)
            lastCheckedTime = currentDate
    if (shouldRunMotionDetection):
        motionState = picam.motion()
        if (motionState):
            camera.takepicture()
            send_mail()
            sleep(1)
