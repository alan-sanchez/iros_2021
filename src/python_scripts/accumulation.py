#!/usr/bin/env python3

import rospy

import numpy as np
from scipy.signal import convolve2d
from math import sqrt
from best_fit import fit
from std_msgs.msg import String, Int16, Float32

from PIL import Image

class Accumulation:
	def __init__(self):
		self.UV_dosage_sub 	   = rospy.Subscriber('UV_dosage', Float32, self.UV_dosage_callback)
		self.vel_regulator_pub = rospy.Publisher('vel_regulator', Float32, queue_size=10)
		self.min_dosage = None

		# import polynomial model from the best_fit python script
		self.model = fit(3, plotter = False)
		self.req_dosage = 1

		self.flag = 1

	def UV_dosage_callback(self,msg):
		self.req_dosage = msg.data
		self.convolution_technique()

	def integral_technique(self):
		## Compute area under the polynomial model. The area represents the total
		## surface irradiance from the flashlight.
		x = np.linspace(0,10,100)
		y = self.model(x)
		Irradiance = np.trapz(y, dx = x[1]) * 2
		# print(Irradiance)

		## The diameter of the lit surface is 20 cm.  If the arm's max velocity is 100cm/s
		## then a point would experience the flashlights irradiance for 0.20 seconds.
		## Resulting in a dosage of 0.2 * Irradiance. The ratio between minimum and
		## required dosage informs how much to reduce translational speed of the EE
		min_dosage = Irradiance * 0.2
		ratio = min_dosage/self.req_dosage

		if ratio > 1:
			vel = 1
		elif ratio < .01:
			vel = .01
		else:
			vel = ratio

		# print(vel)

		self.vel_regulator_pub.publish(vel)

		# the width and height of a pixel is defined as 1 cm.

	def convolution_technique(self):
		# This is the array that adds up the radiation values.
		rows = 21
		columns = 43
		accumulator = np.zeros((rows, columns))

		## Set up the convolution mask. This one is a 21 pixel wide mask where the.
		## values are computed from the best fit model function.
		window = 21
		# Ramped
		ramped_mask = np.zeros((window, window))
		center_r = window/2#round(window/2.0)
		center_c = window/2#round(window/2.0)
		for r in range(window):
			for c in range(window):
				radius_dist = sqrt( (r-center_r)**2 + (c-center_c)**2 )

				if radius_dist > 9:
					ramped_mask[r,c] = 0

				else:
					ramped_mask[r,c] = self.model(radius_dist)

		# print(sum(ramped_mask[10,:]))
		irradiance = sum(ramped_mask[window/2, :])

		## The diameter of the considered disinfecting surface is 20 cm. If the arm's max velocity is 11cm/s
		## then a point would experience the flashlights irradiance for (20/14) seconds.Resulting in a dosage of
		## 1.43 * Irradiance. The ratio between minimum and required dosage informs how much to reduce translational
		## speed of the EE.

		min_dosage = irradiance * 20/11
		ratio = min_dosage/self.req_dosage

		if ratio > 1:
			vel = 1
		elif ratio < .01:
			vel = .01
		else:
			vel = ratio

		print(vel)

		self.vel_regulator_pub.publish(vel)

		# # Swipe the window across the swath, at row 5.  This is a bit special-cased for this example.
		# for c in range(columns - window - 1):
		# 	accumulator[0:window, c:c + window] += ramped_mask
		#
		# # Force it into 8 bit format and save as an image.
		# formatted = (accumulator * 255 / np.max(accumulator)).astype('uint8')
		# Image.fromarray(formatted).save('output.png')
		# im = Image.fromarray(formatted)
		# im.show()
		#
		# formatted = (ramped_mask * 255 / np.max(ramped_mask)).astype('uint8')
		# im = Image.fromarray(formatted)
		# im.show()
		# Image.fromarray(formatted).save('ramped_mask.png')
	


if __name__ == '__main__':
	rospy.init_node('accumulation')
	tech = Accumulation()
	# tech.velocity_regulator()
	# tech.convolution_simulation()
	rospy.spin()
