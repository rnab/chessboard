import RPi.GPIO as GPIO
import chess
import chess.engine
import LEDShiftFunctions as led
import ReedInput as rd
import numpy as np
import os
from time import sleep

led.led_off()

def get_move():
	move=""
	board=rd.read_board2()
	pre_board=board.copy()
	while move=="":
		board=rd.read_board2()
		if abs(board-pre_board).any() >0:
			sleep(0.2)
			board=rd.read_board2()
			if abs(board-pre_board).any() >0:
			#print(rd.convert_board(abs(board-pre_board)))
			#move=rd.convert_board(abs(board-pre_board))
				move=board-pre_board
		pre_board=board.copy()
		sleep(0.1)
	return(move)


engine = chess.engine.SimpleEngine.popen_uci("/usr/games/stockfish")
board = chess.Board()

try:
	while True:
		#User turn
		legal_move = False
		return_move = False
		led.led_off()
		while legal_move is False:
			m1=get_move()
			sleep(0.1)
			if np.sum(m1)==-1:
				led.led_one(-m1)
				m2=get_move()
				to_engine_1=rd.convert_board(abs(m1))
				to_engine_2=rd.convert_board(abs(m2))
				mv=to_engine_1+to_engine_2
				sleep(0.1)
				if np.sum(m2)==1 and np.array_equal(-m2,m1):
					#Move cancelled
					led.led_off()
				elif np.sum(m2)==1 and chess.Move.from_uci(mv) in board.legal_moves:
					#Legal move - progress
					legal_move=True
				else:
					#Force return move
					while return_move is False:
						m3=get_move()
						if np.array_equal(-m3,m1):
							return_move=True
							led.led_off()
		
		#If user enters a valid complete move then the second led lights
		led.led_one(m2)
		print(to_engine_1+to_engine_2)
		board.push_uci(to_engine_1+to_engine_2)
		
		print(to_engine_1)
		print(to_engine_2)
		sleep(1)
		led.led_off()
		print(board)
		
		
		# RECEIVE ENGINE MOVE
		result = engine.play(board, chess.engine.Limit(time=0.1))
		board.push(result.move)
		# COMPUTERS TURN
		print(board)
		print(result.move)
		b1=-rd.convert_move_to_board(str(result.move)[0:2])
		print(b1)
		led.led_one(-b1)
		correct_move=False
		while correct_move is False:
			m1 = get_move()
			sleep(0.1)
			if np.array_equal(m1,b1):
				correct_move=True
		led.led_off()
		b2=rd.convert_move_to_board(str(result.move)[2:4])
		led.led_one(b2)
		correct_move=False
		while correct_move is False:
			m2 = get_move()
			sleep(0.1)
			if np.array_equal(m2,b2):
				correct_move=True
		print('move received ok')
		print(board)
		led.led_off()
		
		

except KeyboardInterrupt:
	print("User Interrupt")
	
finally:
	led.led_off()
	GPIO.cleanup()
