#! /usr/env/bin python

import re, sys, os

def parse():

	Data = [] 

	filename = "Test Tracking Data 1.txt"

	if not os.path.isfile(filename):
		print "[x] File does not exist\n"	
		
	fp = open(filename)

	line = fp.readline()

	while line.strip() != "Position":
		line = fp.readline()

	header = fp.readline().strip().split('\t')
	
	line = fp.readline()

	while line.split():
		line = line.strip().split()
		
		try:
			Data.append({'x': line[1], 'y': line[2], 'z': line[3]})
		except IndexError:
			print line


		line = fp.readline()
	
	return Data

if __name__ == "__main__":
		parse()
