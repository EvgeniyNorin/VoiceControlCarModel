import pyaudio
import wave
import os

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100

class RecordingVoice:



	def record_voice_by_time(self, time, name):
		p = pyaudio.PyAudio()
		stream = p.open(format=FORMAT, 
				channels=CHANNELS,
	            rate=RATE,
	            input=True,
	            frames_per_buffer=CHUNK)
		print("***recording***")
		frames = []

		for i in range(0, int(RATE / CHUNK * time)):
		    data = stream.read(CHUNK)
		    frames.append(data)

		stream.stop_stream()
		stream.close()
		p.terminate()
		wf = wave.open(name, 'wb')
		wf.setnchannels(CHANNELS)
		wf.setsampwidth(p.get_sample_size(FORMAT))
		wf.setframerate(RATE)
		wf.writeframes(b''.join(frames))
		wf.close()	


	def record_voice_by_button(self, name):
		p = pyaudio.PyAudio()
		stream = p.open(format=FORMAT, 
				channels=CHANNELS,
	            rate=RATE,
	            input=True,
	            frames_per_buffer=CHUNK)
		print("***recording***")
		frames = []
		while True:
			try:
			    data = stream.read(CHUNK)
			    frames.append(data)

			except KeyboardInterrupt:
				print("***done recording***")
				break

		stream.stop_stream()
		stream.close()
		p.terminate()
		wf = wave.open(name, 'wb')
		wf.setnchannels(CHANNELS)
		wf.setsampwidth(p.get_sample_size(FORMAT))
		wf.setframerate(RATE)
		wf.writeframes(b''.join(frames))
		wf.close()	


	def begin_record_voice(self, name):
		while True:	
			input_value = raw_input()
			if input_value == "r":
				self.record_voice_by_button(name)
				break

	def delete_prev_version(self, name):
		try:
			os.unlink("./speech.wav")
			print "previous record was deleted"
		except:
			pass


