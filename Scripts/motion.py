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

footagePath = '../../Template Comp.mov'
outputDestination = '../../output/'
scriptDestination = '/Support Files/Scripts/Startup/ReverieScript.jsx' if OP_SYSTEM == 'win32' else ''
AEPATH = '/Support Files/AfterFX.exe' if OP_SYSTEM == 'win32' else ''
rootAdobePath = 'c:/Program Files/Adobe/' if OP_SYSTEM == 'win32' else '/Applications/Adobe/'


def main():
    convert(footagePath)

    AfterEffects = getAfterEffectsPath()

    if not AfterEffects:
        print "[-] Adobe After Effects not found"
        print "[-] Please install Adobe After Effects"
        sys.exit(1)

    copyfile("ReverieScript.jsx", AfterEffects + scriptDestination)
    aeprocess = subprocess.Popen([AfterEffects + AEPATH])


"""
Finds the Adobe After Effects directory
and returns its whole path
this method will work for all versions
"""
def getAfterEffectsPath():

    pattern = re.compile('After Effects')

    for subdir in [d for d in os.listdir(rootAdobePath) if os.path.isdir(rootAdobePath + d)]:
        if pattern.search(subdir):
            #print "[+] Found After Effects at {}".format(rootAdobePath + subdir)
            return rootAdobePath + subdir

    print "[-] Adobe After Effects not found"
    return None


"""
Converts the original footage to a png image sequence
and outputs the sequence to /output directory in
the current working directory
"""
def convert(infile):
    os.mkdir(outputDestination)
    ff = ffmpy.FFmpeg(
	inputs={infile: None},
	outputs={outputDestination + 'image-%03d.png':None}
    )

    print "[+] Converting footage to a png image sequence"
    ff.run()

"""
Removes the previously generated image sequence
"""
def cleanup():
    try:
        rmtree(outputDestination)
    except:
	    print "[-] Error deleting image sequence"


if __name__ == '__main__':
	main()

