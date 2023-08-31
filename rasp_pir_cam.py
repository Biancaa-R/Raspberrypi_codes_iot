import RPi.GPIO as gpio
import os
import time
pir=4
i=0
gpio.setmode(gpio.BCM)
gpio.setup(pir,gpio.IN)

os.system("libcamera-vid -t 3000 -o test.h264")
time.sleep(3)
os.system("vlc test.h264")

try:

	while True:
		while gpio.input(pir):
		
		
			while (i<=2):
				os.system("libcamera-still -o img"+str(i)+".jpg -n 1")
				print("Capturing...",i)
				time.sleep(3)
				i=i+1
		
			i=0
			time.sleep(10)
except KeyboardInterrupt:
	print("program over")

		
			
