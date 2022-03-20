import picamera

print("About to take a picture.")
with picamera.PiCamera() as camera:
    camera.resolution = (1280,720)
    camera.capture("/home/pi/home-sec/newimage.jpg")
print("Picture taken.")