from picamera import PiCamera
from time import sleep

camera = PiCamera()
# camera.rotation = 0 
# camera.start_preview(alpha=200)
# camera.start_preview()
# sleep(5)
# camera.capture('/home/pi/Desktop/image2.jpg')
# camera.stop_preview()

camera.start_preview()
for i in range(2):
    camera.annotate_text = f"Picture nr: {i+1}"
    camera.annotate_text_size = 50
    # camera.image_effect = 'denoise'
    sleep(5)
    camera.capture('/home/pi/Desktop/image%s.jpg' % i)
camera.stop_preview()