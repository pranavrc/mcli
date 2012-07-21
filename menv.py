import pysynth
import pyaudio
import wave
import sys
import os

class mEnv:
	cliInput = ()
	def __init__(self):
		cliInput = input(">>> ")
		pysynth.make_wav(cliInput, fn = 'temp.wav', silent = True)

	def play(self):
		chunk = 1024
		wf = wave.open('temp.wav', 'rb')
		p = pyaudio.PyAudio()

		# open stream
		stream = p.open(format =
	         		p.get_format_from_width(wf.getsampwidth()),
        		        channels = wf.getnchannels(),
		                rate = wf.getframerate(),
		                output = True)

		# read data
		data = wf.readframes(chunk)

		# play stream
		while data != '':
		    stream.write(data)
		    data = wf.readframes(chunk)

		stream.stop_stream()
		stream.close()

		p.terminate()
	
	def removeFile(self):
		os.remove('./temp.wav')

if __name__ == "__main__":
	a = mEnv()
	a.play()
	a.removeFile()

