#! /usr/env/bin python

import re, sys, os
import numpy as np
from scipy import stats



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
			Data.append([line[1], line[2], line[3]])
		except IndexError:
			print line


		line = fp.readline()
	Data = np.asarray(Data)
	Data = Data.astype(np.float)
	return Data

if __name__ == "__main__":
		parse()
