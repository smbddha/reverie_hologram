import cv2
import numpy as np
import math
import os

#Global Vars
new_img_height = 1
new_img_width  = 5
#Number of colors per pixel
pixel_type = 3 

#Takes the created image file, RGB tuple, pixel location in image and changes hte pixel information
def colorPixel (image, rgb_tuple, pixel_index_x, pixel_index_y):
	image [pixel_index_x, pixel_index_y] = [rgb_tuple[0], rgb_tuple[1], rgb_tuple[2]]
	#DEBUG
	#print image [pixel_index_x, pixel_index_y]

#Recieves Position Data (-255, 255) then creates a RGB Tuple accordinging. 
# If larger than 255 in either direction the Blue Pixel acts as a multiplier
def calculateAxisData (position_value):
	red_postiive    = 0
	green_negative  = 0
	blue_multiplier = 0

	#if greater than 255 or -255 then deal with multpier and reset position data
	if (abs (position_value) > 255):
		blue_multiplier = math.trunc (position_value/255)
		position_value  = position_value - (blue_multiplier * 255)
	#IF position is negative stores it in the green pixel as a postive value
	if (position_value < 0):
		green_negative = position_value * (-1)
	#Else adds it to the 
	else :
		red_postiive    = position_value

	#Put all data into tuple
	rgb_tuple = (red_postiive, green_negative, blue_multiplier)

	return rgb_tuple


def newFrameImg (image_height, image_width):
	rbg_count = 3 
	new_image  = np.zeros((new_img_height, new_img_width, rbg_count), np.uint8)
	return new_image

#TEST CASE

frame_number = 0
total_frames = int (raw_input ("Enter total_frames : "))


#Random Array from -255 to 255 for testing
x_axis_data_random = np.random.randint(-255, 255, size = total_frames)
y_axis_data_random = np.random.randint(-255, 255, size = total_frames)
#DEBUG
print x_axis_data_random
print y_axis_data_random

#MAIN
while frame_number < total_frames:

	#create enw temp image
	temp_image    = newFrameImg (new_img_height, new_img_width)
	
	colorPixel (temp_image, calculateAxisData (x_axis_data_random[frame_number]), 0, 0)
	colorPixel (temp_image, calculateAxisData (y_axis_data_random[frame_number]), 0, 1)


	#write out frame with frame number attached
	cv2.imwrite ("temp_frame_" + str (frame_number) +".png", temp_image)
	#DEBUG
	print "Frame Number: " + str (frame_number).rjust (2) + "\t\t" + "X: " + str (temp_image[0,0]).rjust(4) + "\t\t" + "Y: " + str (temp_image[0,1]).rjust(6) 
	#increment the current frame number
	frame_number += 1

	