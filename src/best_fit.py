#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt

ir = [# 0.05, .1, .2, .35, .45, .57, 0.8, 1.11, 1.35, 1.85, 2.29, 2.81, 3.44, 4.24, 5.3, 6.61, 8.2, 11, 14.7, 21.4, 26.3]
      26.3, 21.4, 14.7, 11, 8.2, 6.61, 5.3, 4.24, 3.44, 2.81, 2.29, 1.85, 1.35, 1.11, 0.8, .57, .45, .35, .2, .1, .05]
x = np.linspace(0,1, len(ir))

# mymodel = np.poly1d(np.polyfit(x, ir, 4))
# print(mymodel)

# myline = np.linspace(-1,0,100)

plt.scatter(x, ir)
plt.xlabel('Distance from the Center of Lit Surface (cm)')
plt.ylabel('Irradiance (mW/cm^2)')
plt.title('Distance vs Irradiance')
plt.savefig("Distance_vs_Irradiance.png", bbox_inches='tight')
plt.show()




#
# r = np.linspace(-1,1,5)
# theta = np.linspace(0,2*np.pi,5)
#
# r,theta = np.meshgrid(r,theta)
#

# x, y = np.mgrid[-10:10.05:0.5, -10:10.05:0.5]
# r = np.sqrt(x**2 + y**2)
# # for s in range(r.shape[0]):
# #     r[s] = r[20]
# z = 125.8*r**4 - 329.5*r**3 + 318.8*r**2 - 141.4*r + 26.59
# print(r.shape)
#
# fig, ax = plt.subplots(1,1)
#
# im = ax.imshow(z)
# fig.colorbar(im)
# ax.yaxis.set_major_locator(plt.NullLocator()) # remove y axis ticks
# ax.xaxis.set_major_locator(plt.NullLocator()) # remove x axis ticks
# plt.show()

# import numpy as np
# import matplotlib.pyplot as plt
#
# theta = np.linspace(0, 2*np.pi, 100)
#
# r = np.sqrt(1.0)
#
# x1 = r*np.cos(theta)
# x2 = r*np.sin(theta)
#
# fig, ax = plt.subplots(1)
#
# ax.plot(x1, x2)
# ax.set_aspect(1)
