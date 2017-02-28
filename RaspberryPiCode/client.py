import RPIO
import socket
import distance
from ast import literal_eval as make_tuple
import moves


RPIO.setmode(RPIO.BOARD)


#RPIO.setmode(RPIO.BOARD)
sock = socket.socket()
sock.connect(('192.168.43.182', 48124))
sock.setblocking(0)
move = moves.ModelMoves()

data = []




while True:
        try:
                move.reset_ALL()
                data = sock.recv(1024)
                content = data.decode('utf-8')
                tuple = make_tuple(content)
                time = tuple[len(tuple)-1]
                if len(tuple) == 2:
                        if time > 0:

                                move.arbitrary_directions(tuple[0], time)
                elif len(tuple) == 3:
                        if tuple[0] + tuple[1] != 10 and time>0:
                                move.arbitrary_directions(tuple[0], tuple[1],time)
                                print 1
                RPIO.cleanup()
                data = []
        except socket.error:
                pass



sock.close()


