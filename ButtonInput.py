import RPi.GPIO as GPIO
from time import sleep
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

b1=12
b2=16
b3=20
b4=21

GPIO.setup(b1,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(b2,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(b3,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(b4,GPIO.IN,pull_up_down=GPIO.PUD_UP)

# ~ while True:
	# ~ if GPIO.input(b1)==0:
		# ~ print("b1")
		# ~ sleep(0.1)
	# ~ if GPIO.input(b2)==0:
		# ~ print("b2")
		# ~ sleep(0.1)
	# ~ if GPIO.input(b3)==0:
		# ~ print("b3")
		# ~ sleep(0.1)
	# ~ if GPIO.input(b4)==0:
		# ~ print("b4")
		# ~ sleep(0.1)
