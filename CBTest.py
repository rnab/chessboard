import RPi.GPIO as GPIO
from time import sleep
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
r1 = 14
r2 = 15
r3 = 18

c1 = 16
c2 = 20
c3 = 21

GPIO.setup(r1,GPIO.OUT)
GPIO.setup(r2,GPIO.OUT)
GPIO.setup(r3,GPIO.OUT)

GPIO.output(r1,GPIO.LOW)
GPIO.output(r2,GPIO.LOW)
GPIO.output(r3,GPIO.LOW)

GPIO.setup(c1,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(c2,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(c3,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)



def get_board_input():
	while True:
		GPIO.output(r1,GPIO.HIGH)
		if GPIO.input(c1)==1:
			GPIO.output(r1,GPIO.LOW)
			return("button1")
		GPIO.output(r1,GPIO.LOW)
		GPIO.output(r2,GPIO.HIGH)
		
		if GPIO.input(c2) == 1:
			GPIO.output(r2,GPIO.LOW)
			return("button2")
		GPIO.output(r2,GPIO.LOW)
		GPIO.output(r3,GPIO.HIGH)
		
		if GPIO.input(c3) == 1:
			GPIO.output(r3,GPIO.LOW)
			return("button3")
		GPIO.output(r3,GPIO.LOW)
		
def get_board_stream():
	while True:
		print(get_board_input())
		sleep(0.5)

#get_board_input()
