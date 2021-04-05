import RPi.GPIO as GPIO
import chess
import chess.engine
import LEDShiftFunctions as led
import ReedInput as rd
import numpy as np
import os
from time import sleep

led.led_off()

# ~ try:
	
	# ~ board=rd.read_board2()
	# ~ pre_board=board.copy()
	# ~ while True:
		# ~ led.led_on(abs(board-pre_board),0.5)
		# ~ pre_board=board.copy()
		# ~ board=rd.read_board2()
		# ~ if abs(board-pre_board).any() >0:
			# ~ print(rd.convert_board(abs(board-pre_board)))
			# ~ #print(abs(board-pre_board))
		# ~ #print("over")
			# ~ #if board.all()!=pre_board.all():
				# ~ #print(rd.convert_board(abs(board-pre_board)))


# ~ def get_move():
	# ~ move=""
	# ~ board=rd.read_board2()
	# ~ pre_board=board.copy()
	# ~ while move=="":
		# ~ board=rd.read_board2()
		# ~ if abs(board-pre_board).any() >0:
			# ~ #print(rd.convert_board(abs(board-pre_board)))
			# ~ move=rd.convert_board(abs(board-pre_board))
			# ~ print(board)
			# ~ led.led_on(abs(board-pre_board),0.5)
		# ~ pre_board=board.copy()
		# ~ led.led_off()
	# ~ return(move)


# ~ def get_move():
	# ~ move=""
	# ~ board=rd.read_board2()
	# ~ pre_board=board.copy()
	# ~ #sleep(0.1)
	# ~ while move=="":
		# ~ board=rd.read_board2()
		# ~ if abs(board-pre_board).any() >0:
			# ~ #print(rd.convert_board(abs(board-pre_board)))
			# ~ #move=rd.convert_board(abs(board-pre_board))
			# ~ move=board-pre_board
		# ~ pre_board=board.copy()
		# ~ sleep(0.1)
	# ~ return(move)


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


def make_move(a,b):
	board=rd.convert_move_to_board(a)
	move=""
	while move=="":
		led.led_one(board)
		move=get_move()
		print(move)
	led.led_off()

# ~ try:
	# ~ while True:
		# ~ m1=get_move()
		# ~ m2=get_move()
		# ~ print(str(m1)+str(m2))
	# ~ #make_move('a1','a3')
	# ~ #sleep(4)


engine = chess.engine.SimpleEngine.popen_uci("/usr/games/stockfish")

board = chess.Board()



try:
	while True:
		#User turn
		legal_move = False
		while legal_move is False:
			m1=get_move()
			sleep(0.1)
			if np.sum(m1)==-1: #Add other check conditions
				legal_move=True
		led.led_one(-m1)
		legal_move = False
		while legal_move is False:
			m2=get_move()
			sleep(0.1)
			if np.sum(m2)==1: #Add other check conditions
				legal_move=True
		led.led_one(m2)
		to_engine_1=rd.convert_board(abs(m1))
		to_engine_2=rd.convert_board(abs(m2))
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
		led.led_off()
		
		

except KeyboardInterrupt:
	print("User Interrupt")
	
finally:
	led.led_off()
	GPIO.cleanup()
	
	
# ~ 
		

# ~ board=np.array([[1, 1, 1, 1, 1, 1, 1, 1],
						# ~ [1, 1, 1, 1, 1, 1, 1, 1],
						# ~ [0, 0, 0, 0, 0, 0, 0, 1],
						# ~ [0, 0, 0, 0, 0, 0, 0, 0],
						# ~ [0, 0, 1, 0, 1, 1, 1, 0],
						# ~ [0, 0, 1, 0, 0, 0, 0, 0],
						# ~ [1, 1, 1, 1, 1, 1, 1, 1],
						# ~ [1, 1, 1, 1, 1, 1, 1, 1]])

# ~ board=rd.read_board2()

# ~ led.led_on(board,10)

# ~ led.led_off()

#led.led_off()

#led.led_on(np.ones((8,8)),5)
#led.led_off()




# ~ os.system('clear')
# ~ print(board)

# ~ while True:
	# ~ while True:
		# ~ m1=cb.get_board_input()
		# ~ print(m1)
		# ~ sleep(0.5)
		# ~ m2=cb.get_board_input()
		# ~ print(m2)
		# ~ try:
			# ~ board.push_uci(m1+m2)
		# ~ except Exception:
			# ~ os.system('clear')
			# ~ print(board)
			# ~ continue
		# ~ else:
			# ~ break
	
	# ~ os.system('clear')
	# ~ print(board)

	# ~ sleep(2.0)
	# ~ result = engine.play(board, chess.engine.Limit(time=0.1))
	# ~ board.push(result.move)

	# ~ os.system('clear')
	# ~ print(board)
