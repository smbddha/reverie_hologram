import cv2
import numpy as np
import math
import os

#Global Vars
new_img_height = 1
new_img_width  = 5
#Number of colors per pixel
pixel_type     = 3 
#Max Value for Single pixel not combined RGB
pixel_scale    = 255

#Takes the created image file, RGB tuple, pixel location in image and changes hte pixel information
def colorPixel (image, rgb_tuple, pixel_index_x, pixel_index_y):
	image [pixel_index_x, pixel_index_y] = [rgb_tuple[0], rgb_tuple[1], rgb_tuple[2]]
	#DEBUG
	#print image [pixel_index_x, pixel_index_y]

#Creates a new Image based on a specified height and width. 
def newFrameImg (image_height, image_width):
	rbg_count = 3 
	new_image  = np.zeros((new_img_height, new_img_width, rbg_count), np.uint8)
	return new_image



#Recieves Position Data and encodes it. 
# Red = the smallest units
# Green = 1st multiplier - for values over 255
# Blue  = 2nd multipler  - for values over 255*255
def axisToRGB (position_value):
	red_base            = 0
	green_multiplier_1  = 0
	blue_multiplier_2   = 0

	green_mult_factor   = 255
	blue_mult_factor    = 255*255

	# Put values into 0-255 then multipiers 
	# if position is greater than 255 adjust based on multiplier
	if (position_value > 255):
		#Determine multiplier factor
		green_multiplier_1     = math.trunc (position_value/green_mult_factor)
		#if larger than green pixel value add blue multiplier 
		if (green_multiplier_1 > 255):
			#calculate blue multiplier
			blue_multiplier_2  = math.trunc (position_value/blue_mult_factor)
			#New position value minus the multiplier
			position_value     = position_value - (blue_multiplier_2 * blue_mult_factor)
			#re calculates the green value based on the blue mult 
			green_multiplier_1 = math.trunc (position_value/green_mult_factor)
		#Calculates Red Pixel based on remaing value. 	
		red_base  = position_value - (green_multiplier_1 * 255)
	else :
		red_base  = position_value

	#Put all data into tuple
	rgb_tuple = (red_base, green_multiplier_1, blue_multiplier_2)


	#DEBUG
	#print 'red_base' + str (red_base)
	#print 'Green ' + str (green_multiplier_1)
	#print "Blue: " + str (blue_multiplier_2)

	#print rgb_tuple
	return rgb_tuple

#Takes RGB Pixel and converts it back into position data
def RGBToAxis (rgb_tuple):
	red_base           = rgb_tuple[0]
	green_multiplier_1 = rgb_tuple[1] * pixel_scale
	blue_multiplier_2  = rgb_tuple[2] * pixel_scale * pixel_scale

	position_value = red_base + green_multiplier_1 + blue_multiplier_2
	
	return position_value


#Takes Data combines into RBG Tuple
def projectorToRGB (proj_number, ideal_pallete, curr_pallete):
	#combines them into a tuple to return
	rgb_tuple = (proj_number, ideal_pallete, curr_pallete)
	return rgb_tuple

# Returns current 
def RGBToProjection (rgb_tuple):
	pass

#Fog Pixel Encoder
def fogToRGB (fog_boolean):
	#init value
	red_pixel = 0
	# If Fog is On then chagne Red Pixel Value to Full
	if (fog_boolean = True):
		red_pixel = 255

	#Combine into tuple 
	rgb_tuple = (red_pixel, 0, 0)

	return rgb_tuple

def RGBToFog (rgb_tuple):
	#Boolean Variable to determine if fog is on or not. 
	status = True
	#checks pixel
	if (rgb_tuple[0] = 0):
		status = False
	#returns Boolean Status
	return status


def pixelOutput ():
	pass


def imageSeqToVideo ():
	pass
	

#TEST CASE

#frame_number = 0
#total_frames = int (raw_input ("Enter total_frames : "))




'''
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

'''	