import RPIO
import time
TRIG = 8
ECHO = 10

class DistanceSensor:
	def __init__(self):

		RPIO.setup(TRIG, RPIO.OUT, initial=0)
		RPIO.setup(ECHO, RPIO.IN)


	def check_distance(self):
		RPIO.output(TRIG,1)
		time.sleep(0.00001)
		RPIO.output(TRIG,0)
		while RPIO.input(ECHO) == 0:
		        start = time.time()
		while RPIO.input(ECHO) == 1:
		        stop = time.time()
		# Print distance to object in santimeters. Sound speed = 340 m/s
		return (stop - start) * 17000
		

