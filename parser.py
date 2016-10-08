#! /usr/env/bin python

import re, sys, os

def parse(filename):

	pattern = "\b(\d+)\b"
	
	if os.path.isfile(filename):
		for line in open(filename):

			re.findall(pattern, line)
