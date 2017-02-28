import RPIO
import time
CONST_STRAIGHT = 11
CONST_BACK = 13
CONST_LEFT = 3
CONST_RIGHT = 5
import signal
import distance
import datetime


class ModelMoves:

        def __init__(self):
                self.list_funciton  = {8: self.__move_straight, 2: self.__move_back, 4: self.__move_left, 6: self.__move_right}
                signal.signal(signal.SIGALRM, self.__handle)
                self.dist = DistanceSensor()
                self.break_flag = 0

        def __handle(self, signum, frame):
                print "alarm"
                if self.dist.check_distance < 10:
                        move.reset_ALL()
                        self.break_flag = 1

        def __move_straight(self):
                RPIO.setup(CONST_STRAIGHT, RPIO.OUT, initial=RPIO.LOW)
                signal.setitimer(signal.ITIMER_REAL, 0.01, 0.5)

        def __move_back(self):
                RPIO.setup(CONST_BACK, RPIO.OUT, initial=RPIO.LOW)

        def __move_left(self):
                RPIO.setup(CONST_LEFT, RPIO.OUT, initial=RPIO.LOW)

        def __move_right(self):
                RPIO.setup(CONST_RIGHT, RPIO.OUT, initial=RPIO.LOW)

	def arbitrary_directions(self, *args):
	                self.break_flag = 0
	                for command in args[:len(args)-1]:
	                        self.list_funciton[command]()
	                mark = datetime.datetime.now()
	                while datetime.datetime.now() - mark  < args[len(args)-1]:
	                        if self.break_flag:
	                                break
	                self.reset_ALL()
	                signal.setitimer(signal.ITIMER_REAL, 0.0)




        def __close_GPIO(self, const):
                RPIO.setup(const, RPIO.IN)

        def reset_ALL(self):
                self.__close_GPIO(CONST_STRAIGHT)
                self.__close_GPIO(CONST_RIGHT)
                self.__close_GPIO(CONST_LEFT)
                self.__close_GPIO(CONST_BACK)

                                                                                           