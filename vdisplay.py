#! /usr/env/bin python

from pyvirtualdisplay import Display

xephyr = Display(visible = 1, size = (320, 240)).start()
