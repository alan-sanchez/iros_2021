#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb

x = np.linspace(70,240,18)
x = np.append(x, [[300, 600, 900, 1200, 1500, 1800]])/60
ir = [#21.32, 20.67, 20.44, 20.35, 20.22, 20.11, 20.01,
      19.93, 19.85, 19.76, 19.70, 19.63,
      19.56, 19.51, 19.45, 19.39, 19.33, 19.27, 19.22, 19.17, 19.13, 19.08, 19.02, 18.97,
      18.92, 18.61, 17.38, 16.53, 15.92, 15.42, 14.95]

m,z = np.poly1d(np.polyfit(x, ir, 1))
a,b,c = np.poly1d(np.polyfit(x, ir, 2))
print(a,b,c)
print(len(x), len(ir))




plt.plot(x,ir)
plt.plot(x, m*x + z, 'k')
plt.plot(x, a*x**2 + b*x + c, 'r')
# plt.xlim(-1.25,1.25)
# plt.ylim(-1.25,1.25)

plt.grid(linestyle='--')

plt.xlabel('Exposure Time (sec)')
plt.ylabel('Irradiance (mW/cm^2)')
plt.title('Irradiance vs Time')#
# plt.savefig('Color plot', bbox_inches='tight')
plt.show()
