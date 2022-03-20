import picam

motionState = False
while True:
    motionState = picam.motion()
    print (motionState)