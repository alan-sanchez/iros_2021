#!/usr/bin/env python3


import numpy as np
from scipy.signal import convolve2d
from math import sqrt

from PIL import Image


if __name__ == '__main__':
	# This is the array that adds up the radiation values.
	rows = 20
	columns = 40
	accumulator = np.zeros((rows, columns))

	# Set up the convolution mask.  This one is a 10 pixel wide mask of constant value (1.0).  Note that
	# this is different from the masks used in image processing in that the elements of the mask do not
	# have to add up to 1.
	window = 10
	square_mask = np.ones((window, window))

	# This draws a round mask.
	round_mask = np.zeros((window, window))
	for r in range(window):
		for c in range(window):
			if (r - window / 2) ** 2 + (c - window / 2) ** 2 < (window / 2) ** 2: 
				pass
				round_mask[r, c] = 1.0

	# Ramped
	ramped_mask = np.zeros((window, window))
	for r in range(window):
		for c in range(window):
			ramped_mask[r, c] = 1.0 / (((r - 5) ** 2 + (c - 5) ** 2) + 1.0)

	# Swipe the window across the swath, at row 5.  This is a bit special-cased for this example.
	for c in range(columns - window - 1):
		#accumulator[5:5 + window, c:c + window] += square_mask
		#accumulator[5:5 + window, c:c + window] += round_mask
		accumulator[5:5 + window, c:c + window] += ramped_mask


	# Force it into 8 bit format and save as an image.
	formatted = (accumulator * 255 / np.max(accumulator)).astype('uint8')
	Image.fromarray(formatted).save('output.png')

	# Dump the masks
	formatted = (round_mask * 255 / np.max(round_mask)).astype('uint8')
	Image.fromarray(formatted).save('round_mask.png')

	formatted = (ramped_mask * 255 / np.max(ramped_mask)).astype('uint8')
	Image.fromarray(formatted).save('ramped_mask.png')

