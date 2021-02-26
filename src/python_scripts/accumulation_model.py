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
	columns = 130
	accumulator = np.zeros((rows, columns))
	disinfected = np.zeros((rows, columns))

	model = fit(16, plotter = False)


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

	for r in range(rows):
		for c in range(columns):
			if accumulator[r,c] > 26.5:
				disinfected[r,c] = 1

			else:
				disinfected[r,c] = 0

	# c = plt.Circle((10,10), 5, color='r', fill=False, label='Considered Size of Mask')
	# ticks = ['-10','-9','-8','-7','-6','-5','-4','-3','-2','-1','0','1','2','3','4','5','6','7','8','9','10']
	# fig, ax = plt.subplots(1,1)
	# im = ax.imshow(ramped_mask)
	# clb = fig.colorbar(im)
	# ax.add_patch(c)
	# ax.set_xticks((0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20))
	# ax.set_xticklabels(labels = ticks)
	# ax.set_yticks((0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20))
	# ax.set_yticklabels(labels = ticks)
	# ax.set_xlabel('Distance from the Center of UV Exposed Area (cm)')
	# ax.set_ylabel('Distance from the Center of UV Exposed Area (cm)')
	# ax.set_title(' Mask of UV Light Source')
	# clb.set_label('UV Irradiance (mW/cm^2)',labelpad=15)
	# ax.legend()
	# plt.savefig("ramped_mask_2.png", bbox_inches='tight')

	ticks = [0,10,20,30]
	rect = patches.Rectangle((13.5,14.5), 100,1, linewidth=1, edgecolor='r', facecolor='none',label='Disinfected Region')
	fig, ax1 = plt.subplots(1,1)
	im1 = ax1.imshow(accumulator)
	clb1 = fig.colorbar(im1)
	ax1.add_patch(rect)
	ax1.set_yticks(ticks)
	ax1.set_yticklabels(ticks[::-1])
	ax1.set_xlabel('Length of Coverage (cm)')
	ax1.set_ylabel('Height of Coverage (cm)')
	ax1.set_title('Model of Spanned Mask')
	ax1.legend()
	clb1.set_label('UV Irradiance (mW/cm^2)',labelpad=15)


	# im2 = ax2.imshow(disinfected)
	# clb2 = fig.colorbar(im2)
	# ax2.add_patch(rect)
	# ax2.set_yticks(ticks)
	# ax2.set_yticklabels(ticks[::-1])
	# ax2.set_xlabel('Length of Coverage (cm)')
	# ax2.set_ylabel('Height of Coverage (cm)')
	# ax2.set_title('Model of Spanned Mask')
	# ax2.legend()
	# clb2.set_label('UV Irradiance (mW/cm^2)',labelpad=15)

	plt.subplots_adjust(left = 0.08, bottom = 0.15, right = 1, top =0.45)

	plt.savefig("1D_coverage_model.png", bbox_inches='tight')
	plt.show()
