#!/usr/env/bin python

import sys  
import subprocess
import os
import ffmpy
from shutil import copyfile, rmtree

fpath = "../Template Comp.mov"
dest = '../output/'
scriptPath = "c:/Program Files/Adobe/Adobe After Effects CC 2017/Support Files/Scripts/Startup/ReverieScript.jsx"
aePath = "c:/Program Files/Adobe/Adobe After Effects CC 2017/Support Files/AfterFX.exe"

def main():
	convert(fpath)
	copyfile("ReverieScript.jsx", scriptPath)
	aeprocess = subprocess.Popen([aePath])

	"""
	if file[-3:] != '.png':
		file = convert(file)
	""" 
		
def convert(infile):
	os.mkdir(dest)
	ff = ffmpy.FFmpeg(
		inputs={infile: None},
		outputs={dest + 'image-%03d.png':None}
	)
	ff.run()

def cleanup():
	try:
		rmtree(dest)
	except:
		print "[+] Error deleting image sequence"

if __name__ == '__main__':
	main()

"""
scriptPath = "c:/Program Files/Adobe/Adobe After Effects CC 2017/Support Files/Scripts/Startup/ReverieScript.jsx"

print "[+] Writing script to startup folder"
copyfile("ReverieScript.jsx", scriptPath)

aePath = "c:/Program Files/Adobe/Adobe After Effects CC 2017/Support Files/AfterFX.exe"

print "Opening After Effects"
#aeprocess = subprocess.Popen([aePath, "&&"])

print "After Effects opened"
"""
