#from playsound import playsound
import logging
import wave
import sys
import os

class Sound_builder():

	def Build_Output_Sound(self, directory, input_file, by_who = 'Oleg'):
		logging.basicConfig(filename="Sound_builder.log", level=logging.INFO)
		logging.debug("initializing...")

		input_text = open(input_file,'r').read()

		logging.info("Trying to write input text from {}: {}".format(input_file, input_text))

		outfile = "Output_PooP.wav"
		infiles = []
		data= []

		splited_input_text = input_text.split()

		for word in splited_input_text:
			for ltr in word:
				try:
					#playsound('Oleg/{}.wav'.format(ltr.upper()),True)
					open(directory + "/Sound/{}/{}.wav".format(by_who, ltr.upper()), "r")
					infiles.append(directory + '/Sound/{}/{}.wav'.format(by_who, ltr.upper()))

				except Exception as ex:
					logging.error("Error at symbol {}: ".format(ltr, ex))
					pass
			
			infiles.append(directory + '/Sound/{}/_.wav'.format(by_who))

		for infile in infiles:
			w = wave.open(infile, 'rb')
			data.append( [w.getparams(), w.readframes(w.getnframes())] )
			w.close()

		logging.info("Writing output sound at file: " + outfile)

		output = wave.open(outfile, 'wb')
		output.setparams(data[0][0])

		for i in range(len(data)):
			output.writeframes(data[i][1])
		output.close()

		logging.info("Successful writed output sound at file: " + outfile)
		
		return outfile