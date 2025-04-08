from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview()
sleep(5)
camera.capture('/home/pi/Documents/sws3025/lecture05/image.jpg')
camera.stop_preview()
