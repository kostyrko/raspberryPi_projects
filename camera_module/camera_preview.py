from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.rotation = 0 
# camera.start_preview(alpha=200)
camera.start_preview()
sleep(5)
camera.stop_preview()