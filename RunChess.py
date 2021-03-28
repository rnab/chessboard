import RPi.GPIO as GPIO
import chess
import chess.engine
import LEDShiftFunctions as led
import ReedInput as rd
import numpy as np
import os
from time import sleep

led.led_off()
try:
	while True:
	
		board=rd.read_board2()
	# ~ board=np.array([[0, 0, 0, 0, 0, 0, 0, 0],
						# ~ [0, 0, 0, 0, 0, 0, 0, 0],
						# ~ [0, 0, 0, 0, 0, 0, 0, 1],
						# ~ [0, 0, 0, 0, 0, 0, 0, 0],
						# ~ [0, 0, 1, 0, 1, 0, 0, 0],
						# ~ [0, 0, 0, 0, 0, 0, 0, 0],
						# ~ [0, 0, 0, 0, 1, 0, 1, 0],
						# ~ [1, 1, 1, 1, 1, 1, 1, 1]])
	# ~ board=np.ones((8,8))
	#print(board)
	#led.led_off()
	# ~ sleep(1)
	#sleep(1)
	#led.led_on_all()
	#sleep(5)
	#led.led_off()
		#sleep(0.1)
		led.led_on(board,1)
	#sleep(1)
	#sleep(1)
#led.led_off()
#GPIO.cleanup()
except KeyboardInterrupt:
	print("User Interrupt")
	
finally:
	led.led_off()
	GPIO.cleanup()
# ~ while True:
	# ~ board=rd.read_board2()
	# ~ pre_board=board.copy()
	# ~ sleep(0.5)
	# ~ board=rd.read_board2()
	# ~ if (board!= pre_board).any():
		# ~ #print(board-pre_board)
		# ~ led.led_on(board,1)
		

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



# ~ engine = chess.engine.SimpleEngine.popen_uci("/usr/games/stockfish")

# ~ board = chess.Board()

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
