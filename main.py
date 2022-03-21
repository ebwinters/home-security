from time import sleep
from mail import send_mail
import picam
import camera

motionState = False
while True:
    motionState = picam.motion()
    print (motionState)
    if (motionState):
        camera.takepicture()
        send_mail()
        sleep(2)