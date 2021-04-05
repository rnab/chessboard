import RPi.GPIO as GPIO
import time
import numpy as np
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

c_data=3
a_data=2
clock=17
shift=4

GPIO.setup(a_data,GPIO.OUT)
GPIO.setup(c_data,GPIO.OUT)
GPIO.setup(clock,GPIO.OUT)
GPIO.setup(shift,GPIO.OUT)


def led_off():
	for y in range(8):
		GPIO.output(a_data,GPIO.LOW)
		time.sleep(0.00001)
		GPIO.output(clock,GPIO.HIGH)
		time.sleep(0.00001)
		GPIO.output(clock,GPIO.LOW)
		GPIO.output(a_data,GPIO.LOW)
	GPIO.output(shift,GPIO.HIGH)
	GPIO.output(shift,GPIO.LOW)
	for y in range(8):
		GPIO.output(c_data,GPIO.HIGH)
		time.sleep(0.00001)
		GPIO.output(clock,GPIO.HIGH)            # pull CLOCK pin high
		time.sleep(0.00001)
		GPIO.output(clock,GPIO.LOW)            # pull CLOCK pin down, to send a rising edge
		GPIO.output(c_data,GPIO.LOW)       # clear the DATA pin
	GPIO.output(shift,GPIO.HIGH)      # pull the SHIFT pin high to put the 8 bit data out parallel
	GPIO.output(shift,GPIO.LOW)  

def led_on(board,t):
	x=0
	t_end = time.time() + t
	while time.time()<t_end:
		z= x % 8
		for y in range(0,8):
			if (7-z)==y:
				GPIO.output(a_data,GPIO.HIGH)
			else:
				GPIO.output(a_data,GPIO.LOW)
			if board[z][7-y]==1:
				GPIO.output(c_data,GPIO.LOW)
			else:
				GPIO.output(c_data,GPIO.HIGH)
			time.sleep(0.00000001)
			GPIO.output(clock,GPIO.HIGH)            # pull CLOCK pin high
			time.sleep(0.00000001)
			GPIO.output(clock,GPIO.LOW)            # pull CLOCK pin down, to send a rising edge
			#GPIO.output(c_data,GPIO.HIGH)       # clear the DATA pin
			#GPIO.output(a_data,GPIO.LOW)
		GPIO.output(shift,GPIO.HIGH)      # pull the SHIFT pin high to put the 8 bit data out parallel
		time.sleep(0.00000001)
		GPIO.output(shift,GPIO.LOW)
		x=x+1
		
def led_one(board):
	for z in range(0,8):
		if np.sum(board,0)[7-z]==1:
			GPIO.output(c_data,GPIO.LOW)
		else:
			GPIO.output(c_data,GPIO.HIGH)
		if np.sum(board,1)[7-z]==1:
			GPIO.output(a_data,GPIO.HIGH)
		else:
			GPIO.output(a_data,GPIO.LOW)
		time.sleep(0.00000001)
		GPIO.output(clock,GPIO.HIGH)            # pull CLOCK pin high
		time.sleep(0.00000001)
		GPIO.output(clock,GPIO.LOW)            # pull CLOCK pin down, to send a rising edge
			#GPIO.output(c_data,GPIO.HIGH)       # clear the DATA pin
			#GPIO.output(a_data,GPIO.LOW)
	GPIO.output(shift,GPIO.HIGH)      # pull the SHIFT pin high to put the 8 bit data out parallel
	time.sleep(0.00000001)
	GPIO.output(shift,GPIO.LOW)

# ~ def led_on(board):
	# ~ x=0
	# ~ z= x % 8
	# ~ for y in range(0,8):
		# ~ if (7-z)==y:
			# ~ GPIO.output(a_data,GPIO.HIGH)
		# ~ else:
			# ~ GPIO.output(a_data,GPIO.LOW)
		# ~ if board[z][7-y]==1:
			# ~ GPIO.output(c_data,GPIO.LOW)
		# ~ else:
			# ~ GPIO.output(c_data,GPIO.HIGH)
		# ~ time.sleep(0.00000001)
		# ~ GPIO.output(clock,GPIO.HIGH)            # pull CLOCK pin high
		# ~ time.sleep(0.00000001)
		# ~ GPIO.output(clock,GPIO.LOW)            # pull CLOCK pin down, to send a rising edge
		# ~ #GPIO.output(c_data,GPIO.HIGH)       # clear the DATA pin
		# ~ #GPIO.output(a_data,GPIO.LOW)
	# ~ GPIO.output(shift,GPIO.HIGH)      # pull the SHIFT pin high to put the 8 bit data out parallel
	# ~ time.sleep(0.00000001)
	# ~ GPIO.output(shift,GPIO.LOW)
	# ~ x=x+1




def led_on_all():
	for y in range(0,8):
		GPIO.output(a_data,GPIO.HIGH)
		GPIO.output(c_data,GPIO.LOW)
		time.sleep(0.0001)
		GPIO.output(clock,GPIO.HIGH)            # pull CLOCK pin high
		time.sleep(0.0001)
		GPIO.output(clock,GPIO.LOW)
	GPIO.output(shift,GPIO.HIGH)      # pull the SHIFT pin high to put the 8 bit data out parallel
	time.sleep(0.0001)
	GPIO.output(shift,GPIO.LOW)
		
		
#led_off()
#led_on([0,2],[0,2])
#sleep(5)
#led_off()
#led_on([0],[0])
#sleep(1)
#led_off()

# ~ board=np.zeros((8,8))
# ~ board[0][0]=1
# ~ board[2][4]=1
# ~ board[7][1]=1
# ~ #led_on2(board,3)
# ~ led_on2(board,20)
# ~ led_off()
