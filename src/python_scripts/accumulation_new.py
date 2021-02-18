#!/usr/bin/env python3


import numpy as np
from scipy.signal import convolve2d
from math import sqrt
from best_fit import fit

from PIL import Image


if __name__ == '__main__':
	# This is the array that adds up the radiation values.
	rows = 31
	columns = 115
	accumulator = np.zeros((rows, columns))

	model = fit(3, plotter = False)

	# Set up the convolution mask.  This one is a 5 pixel wide mask of constant value (1.0).  Note that
	# this is different from the masks used in image processing in that the elements of the mask do not
	# have to add up to 1.
	window = 21
	# Ramped
	ramped_mask = np.zeros((window, window))
	center_r = window/2#round(window/2.0)
	center_c = window/2#round(window/2.0)
	for r in range(window):
		for c in range(window):
			radius_dist = sqrt( (r-center_r)**2 + (c-center_c)**2 )

			if radius_dist > 10:
				ramped_mask[r,c] = 0

			else:
				ramped_mask[r,c] = model(radius_dist)

	# Swipe the window across the swath, at row 5.  This is a bit special-cased for this example.
	for c in range(columns - window - 1):
		#accumulator[5:5 + window, c:c + window] += square_mask
		# accumulator[0:window, c:c + window] += ramped_mask
		accumulator[5:5 + window, c:c + window] += ramped_mask


	# Force it into 8 bit format and save as an image.
	formatted = (accumulator * 255 / np.max(accumulator)).astype('uint8')
	# Image.fromarray(formatted).save('output.png')
	im = Image.fromarray(formatted)
	im.show()


	formatted = (ramped_mask * 255 / np.max(ramped_mask)).astype('uint8')
	im = Image.fromarray(formatted)
	im.show()
	# Image.fromarray(formatted).save('ramped_mask.png')
