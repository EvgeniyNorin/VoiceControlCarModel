import socket
import parser
import recording
import os
import wave

RASPBERRY_IP = "192.168.43.182"
PORT =  38126

class RaspberryConnection:
	def __init__(self):
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)		
		self.sock.bind((RASPBERRY_IP, PORT))
		self.sock.listen(1)
		(self.conn, self.addr) = self.sock.accept()                    # self.sock.accept()
		

	def send_msg(self, tuple):	 			#msg format must be DIRECTION/TIME ( like STRAIGHT, 10)#
		self.conn.send(str(tuple))

	def recieve(self):
		_data = self.sock.recv(10)
		return int(_data)

	def close_connection(self):
		self.sock.close()



def main():		
	print "press :rec for begin record, and Ctrl + C for interrupt it"
	print "press :exit for exit"
	record = recording.RecordingVoice()
	parsers = parser.SimpleXmlParser()
	connection = RaspberryConnection()
	break_flag = 0
	while True:
			while True:	
				input_value = raw_input()
				if input_value == ":rec":
					record.record_voice_by_button("speech.wav")
					break
				elif input_value == ":exit":
					break_flag = 1	
					break
				else:
					print "wrong command"

			if break_flag == 1:
				break			
			req = parsers.request()
			print req
			command = parsers.parse(req)
			
			if command != "":
				connection.send_msg(parsers.string_parser(command))
			
		
if __name__ == "__main__":
	main()	
