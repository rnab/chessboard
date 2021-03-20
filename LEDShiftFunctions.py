import RPi.GPIO as GPIO
from time import sleep
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

def led_on(c,r):
	#Set Cathode all high except target
	for y in range(8):
		if y in c:
			GPIO.output(c_data,GPIO.LOW)
		else:
			GPIO.output(c_data,GPIO.HIGH)
		if y in r:
			GPIO.output(a_data,GPIO.HIGH)
		else:
			GPIO.output(a_data,GPIO.LOW)
		sleep(0.001)
		GPIO.output(clock,GPIO.HIGH)            # pull CLOCK pin high
		sleep(0.001)
		GPIO.output(clock,GPIO.LOW)            # pull CLOCK pin down, to send a rising edge
		GPIO.output(c_data,GPIO.LOW)       # clear the DATA pin
	GPIO.output(shift,GPIO.HIGH)      # pull the SHIFT pin high to put the 8 bit data out parallel
	sleep(0.001)
	GPIO.output(shift,GPIO.LOW) 


def led_off():
	for y in range(8):
		GPIO.output(a_data,GPIO.LOW)
		sleep(0.001)
		GPIO.output(clock,GPIO.HIGH)
		sleep(0.001)
		GPIO.output(clock,GPIO.LOW)
		GPIO.output(a_data,GPIO.LOW)
	GPIO.output(shift,GPIO.HIGH)
	GPIO.output(shift,GPIO.LOW)
	for y in range(8):
		GPIO.output(c_data,GPIO.HIGH)
		sleep(0.001)
		GPIO.output(clock,GPIO.HIGH)            # pull CLOCK pin high
		sleep(0.001)
		GPIO.output(clock,GPIO.LOW)            # pull CLOCK pin down, to send a rising edge
		GPIO.output(c_data,GPIO.LOW)       # clear the DATA pin
	GPIO.output(shift,GPIO.HIGH)      # pull the SHIFT pin high to put the 8 bit data out parallel
	GPIO.output(shift,GPIO.LOW)  

#led_off()
#led_on([0,2],[0,2])
#sleep(5)
#led_off()
#led_on([0],[0])
#sleep(1)
#led_off()
