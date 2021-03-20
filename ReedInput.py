import RPi.GPIO as GPIO
from time import sleep
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
import LEDShiftFunctions as led


cols={27:'h',22:'g',10:'f',9:'e',11:'d',5:'c',6:'b',13:'a'}
rows={14:'1',15:'2',18:'3',23:'4',24:'5',25:'6',8:'7',7:'8'}
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

def read_board():
	board=[0]*64
	i=0
	for c in cols.keys():
		GPIO.setup(c,GPIO.OUT)
		GPIO.output(c,GPIO.LOW)
	for r in rows.keys():
		GPIO.setup(r,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
	
	for c in cols.keys():
		GPIO.output(c,GPIO.HIGH)
		for r in rows.keys():
			if GPIO.input(r)==1:
				board[i]=1
			else:
				board[i]=0
			i=i+1
			sleep(0.0001)
		GPIO.output(c,GPIO.LOW)
	return(board)

def get_rc(board):
	led.led_off()
	z=0
	for i in board:
		if i == 1:
			led.led_on([int(z/8)],[z%8])
			sleep(0.1)
		z=z+1


while True:
	board=read_board()
	get_rc(board)
