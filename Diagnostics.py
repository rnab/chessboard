import RPi.GPIO as GPIO
import LEDShiftFunctions as led
import ReedInput as rd
import numpy as np
import os
from time import sleep

led.led_off()

board=np.zeros((8,8))

for i in range(0,8):
	for j in range(0,8):
		board[i,j]=1
		led.led_on(board,0.01)

led.led_on(np.ones((8,8)),2)

led.led_off()

try:
	board=rd.read_board2()
	pre_board=board.copy()
	while True:
		pre_board=board.copy()
		while board.all()==pre_board.all():
			print(board)
			led.led_on(board,1)
			board=rd.read_board2()
			os.system('clear')



except KeyboardInterrupt:
	print("User Interrupt")
	
finally:
	led.led_off()
	GPIO.cleanup()
	
