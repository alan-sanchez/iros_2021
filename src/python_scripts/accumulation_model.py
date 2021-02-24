#!/usr/bin/env python3

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from scipy.signal import convolve2d
from math import sqrt
from best_fit import fit

from PIL import Image


if __name__ == '__main__':
	# This is the array that adds up the radiation values.
	rows = 31
	columns = 131
	accumulator = np.zeros((rows, columns))

	model = fit(3, plotter = False)

	# Set up the convolution mask.  This one is a 5 pixel wide mask of constant value (1.0).  Note that
	# this is different from the masks used in image processing in that the elements of the mask do not
	# have to add up to 1.
	window = 21

	#time_exposure is the diameter of exposed area divided by max velocity.
	minimum_time_exposure = .1
	req_dosage = 2.7 #mJ/cm^2

	ramped_mask = np.zeros((window, window))
	center_r = window/2
	center_c = window/2
	for r in range(window):
		for c in range(window):
			radius_dist = sqrt( (r-center_r)**2 + (c-center_c)**2 )

			if radius_dist > 10:
				ramped_mask[r,c] = 0

			else:
				ramped_mask[r,c] = model(radius_dist)
	print(sum(ramped_mask[10,5:16]))
	uv_dose = sum(ramped_mask[10,5:16])*minimum_time_exposure
	ratio = uv_dose/req_dosage
	print(ratio)

	# Swipe the window across the swath, at row 5.  This is a bit special-cased for this example.
	for c in range(columns - window - 1):
		#accumulator[5:5 + window, c:c + window] += square_mask
		# accumulator[0:window, c:c + window] += ramped_mask
		accumulator[5:5+window, c:c + window] += ramped_mask/ratio

	# c = plt.Circle((10,10), 5, color='r', fill=False, label='UV Cutoff Diameter')
	# ticks = ['-10','-9','-8','-7','-6','-5','-4','-3','-2','-1','0','1','2','3','4','5','6','7','8','9','10']
	# fig, ax = plt.subplots(1,1)
	# im = ax.imshow(ramped_mask)
	# fig.colorbar(im)
	# ax.add_patch(c)
	# ax.set_xticks((0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20))
	# ax.set_xticklabels(labels = ticks)
	# ax.set_yticks((0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20))
	# ax.set_yticklabels(labels = ticks)
	# ax.set_xlabel('Distance from the Center of UV Exposed Area (cm)')
	# ax.set_ylabel('Distance from the Center of UV Exposed Area (cm)')
	# ax.set_title('Ramped Mask Model of UV Light Source')
	# ax.legend()
	#
	# plt.show()

	rect = patches.Rectangle((14,14), 100,2, linewidth=1, edgecolor='r', facecolor='none',label='Region')
	fig, ax = plt.subplots(1,1)
	im = ax.imshow(accumulator)
	fig.colorbar(im)
	ax.add_patch(rect)
	ax.set_xlabel('Length of 1-D Coverage (cm)')
	ax.set_ylabel('Height of 1-D Coverage (cm)')
	ax.set_title('Reduction of ')
	ax.legend()

	plt.show()
