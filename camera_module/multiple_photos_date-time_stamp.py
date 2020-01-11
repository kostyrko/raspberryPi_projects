from picamera import PiCamera, Color
from time import sleep
import time
import datetime


camera = PiCamera()
# camera.resolution = (2592, 1944)
# camera.framerate = 15
# camera.rotation = 180
camera.annotate_text_size = 30
camera.annotate_foreground = Color('white')
camera.start_preview()
for i in range(2):
    sleep(2)
    camera.annotate_text = (time.strftime('%H:%M:%S',time.localtime())+
    " ("+datetime.date.today().isoformat()+")")
    camera.capture('/home/pi/Desktop/image%s.jpg' % i)
camera.stop_preview()
