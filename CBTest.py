import RPi.GPIO as GPIO
from time import sleep
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

cols={21:'h',20:'g',16:'f',12:'e',1:'d',18:'c',15:'b',14:'a'}
#rows={19:'1',13:'2',6:'3',5:'4',0:'5',4:'8',3:'6',2:'7'}

cols={21:'h',20:'g',16:'f',12:'e',1:'d',18:'c',15:'b',14:'a'}
rows={19:'1',13:'2',6:'3',5:'4',0:'5',4:'8',22:'6',27:'7'}

#Set up GPIO

def get_board_input():
	for c in cols.keys():
		GPIO.setup(c,GPIO.OUT)
		GPIO.output(c,GPIO.LOW)

	for r in rows.keys():
		GPIO.setup(r,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
	
	while True:
		for c in cols.keys():
			GPIO.output(c,GPIO.HIGH)
			for r in rows.keys():
				if GPIO.input(r)==1:
					return(cols[c]+rows[r])
				sleep(0.001)
			GPIO.output(c,GPIO.LOW)

		
def get_board_stream():
	while True:
		print(get_board_input())
		sleep(0.1)

#get_board_stream()
