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
	m1=cb.get_board_input()

	if m1=="button1":
		board.push_san("d2d4")
	elif m1=="button2":
		board.push_san("e2e4")
	elif m1=="button3":
		board.push_uci("g1f3")
	
	os.system('clear')
	print(board)

	sleep(1.0)
	result = engine.play(board, chess.engine.Limit(time=0.1))
	board.push(result.move)

	os.system('clear')
	print(board)
