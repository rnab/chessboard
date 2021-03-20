import RPi.GPIO as GPIO
from time import sleep
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

cols={17:'a',27:'b',22:'c',10:'d',9:'e',11:'f',5:'g',6:'h'}
rows={23:'1',24:'2',25:'3',8:'4',7:'5',1:'6',12:'7',16:'8'}

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
					sleep(0.005)
			GPIO.output(c,GPIO.LOW)

def get_board_stream():
	while True:
		print(get_board_input())
		sleep(0.1)

get_board_stream()
