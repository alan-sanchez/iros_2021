#!/usr/bin/env python3

import matplotlib.pyplot as plt
import matplotlib.patches as patches
# plt.rcParams.update({'font.size': 12})

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
				disinfected[r,c] = accumulator[r,c] # or 1

			else:
				disinfected[r,c] = 0

	print(np.amax(disinfected))
	# print(max(disinfected))
	# c = plt.Circle((10,10), 5, color='r',linewidth=2, fill=False, label='Considered Size of Kernel Mask')
	# ticks = ['-10','-9','-8','-7','-6','-5','-4','-3','-2','-1','0','1','2','3','4','5','6','7','8','9','10']
	# fig, ax = plt.subplots(1,1)
	# im = ax.imshow(ramped_mask)
	# clb = fig.colorbar(im)
	# ax.add_patch(c)
	# ax.set_xticks((0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20))
	# ax.set_xticklabels(labels = ticks)
	# ax.set_yticks((0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20))
	# ax.set_yticklabels(labels = ticks)
	# ax.set_xlabel('Distance from the Center of UV Exposed Area ($cm$)',fontsize=12)
	# ax.set_ylabel('Distance from the Center of UV Exposed Area ($cm$)',fontsize=12)
	# ax.set_title(' Mask of UV Light Source',fontsize=18)
	# clb.set_label('UV Irradiance $(mW/cm^2)$',labelpad=15,fontsize=16)
	# ax.legend()
	# plt.savefig("ramped_mask_2.png", bbox_inches='tight')

	ticks = [0,10,20,30]
	rect = patches.Rectangle((13.5,14.5), 100,1, linewidth=2, edgecolor='r', facecolor='none',label='Disinfected Region')
	fig, ax1 = plt.subplots(1,1)
	fig.set_size_inches(10.25, 6.25)

	im1 = ax1.imshow(accumulator)
	clb1 = fig.colorbar(im1)
	ax1.add_patch(rect)
	ax1.set_yticks(ticks)
	ax1.set_yticklabels(ticks[::-1])
	ax1.set_xlabel('Length ($cm$)', fontsize=30)
	ax1.set_ylabel('Height ($cm$)',  fontsize=30)
	ax1.set_title('Ebola Sudan, $k$ = 0.0867 $m^2/J$ at $D_{90}$ ',y=1.3 ,fontsize=30)
	ax1.legend(fontsize=15)
	clb1.set_label('UV Irradiance ($mW/cm^2$)',labelpad=15, fontsize=24)
	plt.subplots_adjust(left = 0.12, bottom = 0.22, right = 1, top =0.80)
	plt.savefig("1D_coverage_model.png", bbox_inches='tight')


	plt.show()
