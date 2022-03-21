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
    currentDate = datetime.datetime.now()
    if currentDate.second >= 58 and currentDate.second <= 60:
        if lastCheckedTime < currentDate:
            shouldRunMotionDetection = tableStorage.GetShouldMonitorFlag()
            sleep(2)
            lastCheckedTime = currentDate
    if (shouldRunMotionDetection):
        motionState = picam.motion()
        if (motionState):
            camera.takepicture()
            send_mail()
            sleep(1)
