import picam
import camera

motionState = False
while True:
    motionState = picam.motion()
    print (motionState)

    if (motionState):
        camera.takepicture()