#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb

x = np.linspace(0,240,25)
x = np.append(x, [[300, 600, 900, 1200, 1500, 1800]])/60
ir_1 = [21.32, 20.67, 20.44, 20.35, 20.22, 20.11, 20.01, 19.93, 19.85, 19.76, 19.70, 19.63,
        19.56, 19.51, 19.45, 19.39, 19.33, 19.27, 19.22, 19.17, 19.13, 19.08, 19.02, 18.97,
        18.92, 18.61, 17.38, 16.53, 15.92, 15.42, 14.95]

ir_2 = [20.65, 20.33, 20.24, 20.12, 20.04, 19.94, 19.86, 19.79, 19.70, 19.64, 19.58, 19.51,
        19.44, 19.38, 19.32, 19.25, 19.19, 19.14, 19.08, 19.02, 18.97, 18.93, 18.87, 18.82,
        18.77, 18.49, 17.26, 16.44, 15.97, 15.50, 15.12]

ir_3 = [17.05, 16.75, 16.56, 16.43, 16.32, 16.21, 16.13, 16.05, 15.97, 15.91, 15.84, 15.77,
        15.71, 15.65, 15.60, 15.54, 15.49, 15.43, 15.38, 15.34, 15.29, 15.24, 15.20, 15.15,
        15.10, 14.85, 13.78, 12.89, 12.26, 11.73, 11.19]
# m,z = np.poly1d(np.polyfit(x, ir_1, 1))
# a,b,c = np.poly1d(np.polyfit(x, ir_1, 2))
# print(a,b,c)
# print(len(x), len(ir))




plt.plot(x,ir_1)
plt.plot(x,ir_2, 'r')
plt.plot(x,ir_3, 'k')
# plt.plot(x, m*x + z, 'k')
# plt.plot(x, a*x**2 + b*x + c, 'r')
# plt.xlim(-1.25,1.25)
# plt.ylim(-1.25,1.25)

plt.grid(linestyle='--')

plt.xlabel('Exposure Time (min)')
plt.ylabel('Irradiance (mW/cm^2)')
plt.title('Irradiance vs Time')#
# plt.savefig('Color plot', bbox_inches='tight')
plt.show()
