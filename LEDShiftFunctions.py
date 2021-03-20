import RPi.GPIO as GPIO
from time import sleep
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

c_data=3
a_data=2
c_clock=17
a_clock=17
c_shift=4
a_shift=4

GPIO.setup(a_data,GPIO.OUT)
GPIO.setup(c_data,GPIO.OUT)
GPIO.setup(a_clock,GPIO.OUT)
GPIO.setup(c_clock,GPIO.OUT)
GPIO.setup(a_shift,GPIO.OUT)
GPIO.setup(c_shift,GPIO.OUT)

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
		GPIO.output(c_clock,GPIO.HIGH)            # pull CLOCK pin high
		sleep(0.001)
		GPIO.output(c_clock,GPIO.LOW)            # pull CLOCK pin down, to send a rising edge
		GPIO.output(c_data,GPIO.LOW)       # clear the DATA pin
	GPIO.output(c_shift,GPIO.HIGH)      # pull the SHIFT pin high to put the 8 bit data out parallel
	sleep(0.001)
	GPIO.output(c_shift,GPIO.LOW) 


def led_off():
	for y in range(8):
		GPIO.output(a_data,GPIO.LOW)
		sleep(0.001)
		GPIO.output(a_clock,GPIO.HIGH)
		sleep(0.001)
		GPIO.output(a_clock,GPIO.LOW)
		GPIO.output(a_data,GPIO.LOW)
	GPIO.output(a_shift,GPIO.HIGH)
	GPIO.output(a_shift,GPIO.LOW)
	for y in range(8):
		GPIO.output(c_data,GPIO.HIGH)
		sleep(0.001)
		GPIO.output(c_clock,GPIO.HIGH)            # pull CLOCK pin high
		sleep(0.001)
		GPIO.output(c_clock,GPIO.LOW)            # pull CLOCK pin down, to send a rising edge
		GPIO.output(c_data,GPIO.LOW)       # clear the DATA pin
	GPIO.output(c_shift,GPIO.HIGH)      # pull the SHIFT pin high to put the 8 bit data out parallel
	GPIO.output(c_shift,GPIO.LOW)  

led_off()
led_on([0,1,2,3,4,5,6,7],[0,1,2,3,4,5,6,7])
sleep(5)
led_off()
led_on([0],[0])
sleep(1)
led_off()
