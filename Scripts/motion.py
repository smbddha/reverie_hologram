#!/usr/env/bin python
#############################################################################
#                                                                           #
#                                                                           #
# motion.py                                                                 #
#                                                                           #
# Converts footage to png sequence then imports it into                     #
# Adobe After Effects, where Mocha must then be open to motion              #
# track the actor in the footage                                            #
#                                                                           #
#############################################################################

import sys
import subprocess
import os
import ffmpy
import re
from shutil import copyfile, rmtree

OP_SYSTEM = sys.platform

fpath = '../Template Comp.mov'
outputDestination = '../output/'
scriptDestination = '/Support Files/Scripts/Startup/ReverieScript.jsx'
rootAdobePath = 'c:/Program Files/Adobe/' if OP_SYSTEM == 'win32' else '/Applications/Adobe/'

def main():
    convert(fpath)
    copyfile("ReverieScript.jsx", rootAdobePath + scriptPath)
    aeprocess = subprocess.Popen([aePath])


def getAfterEffectsPath():

    pattern = re.compile("After Effects")

    for subdir in [d for d in os.listdir(rootAdobePath) if os.path.isdir(rootAdobePath + f)]:
        if pattern.search(d):
            print "[+] Found After Effects at {}".format(rootAdobePath + d)
            return rootAdobePath + d

    print "[-] Adobe After Effects not found"
    return


def convert(infile):
    os.mkdir(dest)
    ff = ffmpy.FFmpeg(
	inputs={infile: None},
	outputs={dest + 'image-%03d.png':None}
    )

    print "[+] Converting footage to a png image sequence"
    ff.run()

def cleanup():
    try:
        rmtree(dest)
    except:
	print "[-] Error deleting image sequence"


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
