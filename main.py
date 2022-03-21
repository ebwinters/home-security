from time import sleep
from mail import send_fb_message, send_mail
import picam
import camera

motionState = False
while True:
    motionState = picam.motion()
    print (motionState)
    send_fb_message()
    if (motionState):
        camera.takepicture()
        send_mail()
        sleep(2)