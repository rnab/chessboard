import chess
import chess.engine
import CBTest as cb
import os
from time import sleep

engine = chess.engine.SimpleEngine.popen_uci("/usr/games/stockfish")

board = chess.Board()

os.system('clear')
print(board)

while True:
	while True:
		m1=cb.get_board_input()
		print(m1)
		sleep(0.5)
		m2=cb.get_board_input()
		print(m2)
		try:
			board.push_uci(m1+m2)
		except Exception:
			os.system('clear')
			print(board)
			continue
		else:
			break
	
	os.system('clear')
	print(board)

	sleep(2.0)
	result = engine.play(board, chess.engine.Limit(time=0.1))
	board.push(result.move)

	os.system('clear')
	print(board)
