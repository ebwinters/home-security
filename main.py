from time import sleep
from mail import send_mail
import picam
import camera
import datetime
from table_storage import TableStorage

tableStorage = TableStorage("homesecflags")
motionState = False
lastCheckedTime = datetime.datetime.now()
shouldRunMotionDetection = True
while True:
    if lastCheckedTime < datetime.datetime.now():
        shouldRunMotionDetection = tableStorage.GetShouldMonitorFlag()
        lastCheckedTime = datetime.datetime.now()
    motionState = picam.motion()
    print (motionState)
    if (motionState):
        camera.takepicture()
        send_mail()
        sleep(1)
