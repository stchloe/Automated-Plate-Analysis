from picamera2 import Picamera2, Preview
import time

# open camera & take pic
picam2 = Picamera2()
picam2.start_and_capture_file("test1.jpg")
print("we have taken a pic")

# neatly shutdown camera
picam2.stop_preview()
picam2.stop()