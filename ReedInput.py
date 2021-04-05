import RPi.GPIO as GPIO
from time import sleep
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
import LEDShiftFunctions as led
import numpy as np


rows={27:'h',22:'g',10:'f',9:'e',11:'d',5:'c',6:'b',13:'a'}
cols={14:'1',15:'2',18:'3',23:'4',24:'5',25:'6',1:'7',7:'8'}

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


#while True:
#	board=read_board()
#	get_rc(board)

def read_board2():
	board=np.zeros((8,8))
	
	for c in cols.keys():
		GPIO.setup(c,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
	
	for r in rows.keys():
		GPIO.setup(r,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
		
	x=7
	for c in cols.keys():
		y=7
		GPIO.setup(c,GPIO.OUT)
		GPIO.output(c,GPIO.HIGH)
		sleep(0.001)
		for r in rows.keys():
			if GPIO.input(r)==1:
				board[x][y]=1
			else:
				board[x][y]=0
			y=y-1
			#print(GPIO.input(r))
			sleep(0.001)
		x=x-1
		GPIO.output(c,GPIO.LOW)
		GPIO.setup(c,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
		sleep(0.001)
	return(board)


#while True:
#	board=read_board2()
#	get_rc(board)

def convert_board(board):
	realboard=np.array([['a8', 'b8', 'c8', 'd8', 'e8', 'f8', 'g8', 'h8'],
						['a7', 'b7', 'c7', 'd7', 'e7', 'f7', 'g7', 'h7'],
						['a6', 'b6', 'c6', 'd6', 'e6', 'f6', 'g6', 'h6'],
						['a5', 'b5', 'c5', 'd5', 'e5', 'f5', 'g5', 'h5'],
						['a4', 'b4', 'c4', 'd4', 'e4', 'f4', 'g4', 'h4'],
						['a3', 'b3', 'c3', 'd3', 'e3', 'f3', 'g3', 'h3'],
						['a2', 'b2', 'c2', 'd2', 'e2', 'f2', 'g2', 'h2'],
						['a1', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h1']])
	return realboard[board==1][0]


def convert_move_to_board(s):
	realboard=np.array([['a8', 'b8', 'c8', 'd8', 'e8', 'f8', 'g8', 'h8'],
						['a7', 'b7', 'c7', 'd7', 'e7', 'f7', 'g7', 'h7'],
						['a6', 'b6', 'c6', 'd6', 'e6', 'f6', 'g6', 'h6'],
						['a5', 'b5', 'c5', 'd5', 'e5', 'f5', 'g5', 'h5'],
						['a4', 'b4', 'c4', 'd4', 'e4', 'f4', 'g4', 'h4'],
						['a3', 'b3', 'c3', 'd3', 'e3', 'f3', 'g3', 'h3'],
						['a2', 'b2', 'c2', 'd2', 'e2', 'f2', 'g2', 'h2'],
						['a1', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h1']])
	return ((realboard==s).astype(int))

# ~ while True:
	# ~ board=read_board2()
	# ~ pre_board=board.copy()
	# ~ sleep(0.5)
	# ~ board=read_board2()
	# ~ if (board!= pre_board).any():
		# ~ #print(board-pre_board)
		# ~ print(convert_board(abs(board-pre_board)))


