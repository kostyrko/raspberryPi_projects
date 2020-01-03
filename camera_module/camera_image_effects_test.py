''' simple  script testing possible image effects
for Raspberry Pi camera module, saves filtered images as jpg
after https://projects.raspberrypi.org/en/projects/getting-started-with-picamera'''

from picamera import PiCamera
from time import sleep

camera = PiCamera()

# begain camera preview with opacity of 180 (max. 255)
camera.start_preview(alpha=180)

for effect in camera.IMAGE_EFFECTS:
    camera.image_effect = effect
    #text description on the top of an image
    camera.annotate_text = "Effect: %s" % effect
    sleep(2)
    camera.capture('/home/pi/Desktop/image_%s.jpg' % effect)
# after the loop is finished end preview
camera.stop_preview()