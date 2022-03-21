import picamera

def takepicture():
    print("About to take a picture.")
    with picamera.PiCamera() as camera:
        camera.resolution = (1280,720)
        camera.capture("/home/pi/pi-camera-stream-flask/static/newimage.jpg")
    print("Picture taken.")