import numpy

def parserTrackingData (filename):
	location_data = numpy.zeros ((1000, 2),  dtype=numpy.int)
	f = open (filename, 'r')
	output = open ("output.txt", 'w')
	index = 0

#

	while 1:
		text = f.readline ()
		# exit status
		exit = False
		if 'Position' in text:
			#skip the header
			header = f.readline()
			#grabs the first data information
			sub_text = f.readline()
			location_data = numpy.zeros ((1, 2),  dtype=numpy.int)
			while sub_text != '\n':
				sub_text = sub_text[1:]
				print (sub_text)
				#print (index)
				#location_data [index][0] =
				#location_data [index][1] =
				sub_text = f.readline()
				index += 1

				if sub_text == '\n':
					#Change Exit Status and then break
					exit = True
					break
		#Breaks Loop if Exit
		if exit == True:
			break

	f.close()

parserTrackingData ("Test Tracking Data 1.txt")
