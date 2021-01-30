import RPi.GPIO as GPIO
from time import sleep
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
#Set Button and LED pins
r1 = 14
r2 = 15
r3 = 18

c1 = 16
c2 = 20
c3 = 21

#Setup Button and LED
GPIO.setup(r1,GPIO.OUT)
GPIO.setup(r2,GPIO.OUT)
GPIO.setup(r3,GPIO.OUT)

GPIO.output(r1,GPIO.LOW)
GPIO.output(r2,GPIO.LOW)
GPIO.output(r3,GPIO.LOW)

GPIO.setup(c1,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(c2,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(c3,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

#flag = 0

while True:
	GPIO.output(r1,GPIO.HIGH)
	if GPIO.input(c1) == 1:
		print("button1")
	#sleep(0.1)
	GPIO.output(r1,GPIO.LOW)
	GPIO.output(r2,GPIO.HIGH)
	if GPIO.input(c2) == 1:
		print("button2")
	#sleep(0.1)
	
	GPIO.output(r2,GPIO.LOW)
	GPIO.output(r3,GPIO.HIGH)
	if GPIO.input(c3) == 1:
		print("button3")
	#sleep(0.1)
	GPIO.output(r3,GPIO.LOW)
	sleep(0.1)
