import RPi.GPIO as GPIO
import chess
import chess.engine
import LEDShiftFunctions as led
import ReedInput as rd
import numpy as np
import os
import ButtonInput as bt
from time import sleep

led.led_off()

#Set up button input
b1=12
b2=16
b3=20
b4=21

GPIO.setup(b1,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(b2,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(b3,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(b4,GPIO.IN,pull_up_down=GPIO.PUD_UP)


def get_move():
	move=np.zeros((8,8))
	board=rd.read_board2()
	pre_board=board.copy()
	while np.array_equal(move,np.zeros((8,8))) and GPIO.input(b1)==1 and GPIO.input(b4)==1:
		board=rd.read_board2()
		if np.array_equal(board,pre_board) == False:
			sleep(0.2)
			board2=rd.read_board2()
			#Because of noise in the GPIO inputs we require two readings of the change,
			#0.2s apart to record as an actual change to the board
			if np.array_equal(board,board2):
			#if abs(board-pre_board).any() >0:
			#print(rd.convert_board(abs(board-pre_board)))
			#move=rd.convert_board(abs(board-pre_board))
				move=board-pre_board
		#pre_board=board.copy()
		sleep(0.01)
	if GPIO.input(b1)==0:
		move=np.ones((8,8))
	if GPIO.input(b4)==0:
		print("Quit")
		quit()
	print(move)
	return(move)


def user_move(board):
	legal_move = False
	return_move = False
	led.led_off()
	while legal_move is False:
		m1=get_move()
		#sleep(0.1)
		
		if np.sum(m1)==-1:
			led.led_one(-m1)
			m2=get_move()
			to_engine_1=rd.convert_board(abs(m1))
			to_engine_2=rd.convert_board(abs(m2))
			mv=to_engine_1+to_engine_2
			sleep(0.01)
			if np.sum(m2)==1 and np.array_equal(-m2,m1):
				#Move cancelled
				led.led_off()
			elif np.sum(m2)==1 and chess.Move.from_uci(mv) in board.legal_moves:
				#Legal move - progress
				legal_move=True
				led.led_one(m2)
				board.push_uci(mv)
			else:
				#Force return move
				while return_move is False:
					m3=get_move()
					if np.array_equal(-m3,m1):
						return_move=True
						led.led_off()
		elif np.array_equal(m1,np.ones((8,8))):
			#if we get a null move from the button press, exit the loop
			legal_move=True
	sleep(1)
	led.led_off()
	return(0)


def computer_move(board):
	result = engine.play(board, chess.engine.Limit(time=0.1))
	board.push(result.move)
	# COMPUTERS TURN
	b1=-rd.convert_move_to_board(str(result.move)[0:2])
	led.led_one(-b1)
	correct_move=False
	while correct_move is False:
		m1 = get_move()
		sleep(0.01)
		if np.array_equal(m1,b1):
			correct_move=True
	led.led_off()
	b2=rd.convert_move_to_board(str(result.move)[2:4])
	led.led_one(b2)
	correct_move=False
	while correct_move is False:
		m2 = get_move()
		sleep(0.01)
		if np.array_equal(m2,b2):
			correct_move=True
	led.led_off()


engine = chess.engine.SimpleEngine.popen_uci("/usr/games/stockfish")
board = chess.Board()

def init_board():
	#led.led_N(1)
	start_pos=np.array( [[0,0,0,0,0,0,0,0],
						[0,0,0,0,0,0,0,0],
						[0,0,0,0,0,0,0,0],
						[0,0,0,0,0,0,0,0],
						[0,0,0,0,0,0,0,0],
						[0,0,0,0,0,0,0,0],
						[0,0,0,0,0,0,1,1],
						[0,0,0,0,0,0,1,1]])
	board=rd.read_board2()
	while np.array_equal(board,start_pos)==False:
		board=rd.read_board2()
		led.led_on(start_pos - board ,1)
	print("Setup complete")				




try:
	init_board()
	led.lightshow_2()
	while board.is_game_over()==False:
		user_move(board)
		os.system('clear')
		print(board)
		computer_move(board)
		os.system('clear')
		print(board)
	print("game over")


except KeyboardInterrupt:
	print("User Interrupt")
	
finally:
	led.led_off()
	GPIO.cleanup()
