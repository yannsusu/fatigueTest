from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview()
camera.start_recording('/home/pi/Documents/sws3025/lecture05/video.h264')
sleep(10)
camera.stop_recording()
camera.stop_preview()