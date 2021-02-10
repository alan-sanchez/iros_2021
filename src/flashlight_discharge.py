#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb

x = np.linspace(0,390,40)
x = np.append(x, [[480, 600, 900, 1200, 1500, 1800]])/60
y = [12.09, 11.42, 11.08, 10.82, 10.62, 10.45, 10.29, 10.15, 10.01, 9.71,
      9.23,  8.79,  8.25,  7.89,  7.45,  7.20,  7.20,  7.18,  7.16, 7.15,
      7.13,  7.11,  7.09,  7.07,  7.05,  7.02,  7.00,  6.99, 6.96, 6.95,
      6.92, 6.90, 6.88, 6.86, 6.84, 6.82,6.80, 6.79, 6.77, 6.75, 6.58,
      6.4, 6.06,5.74, 5.56, 5.51 ]
print(type(x))
plt.scatter(x,y)
# plt.xlim(-1.25,1.25)
# plt.ylim(-1.25,1.25)

plt.grid(linestyle='--')

plt.xlabel('Exposure Time (sec)')
plt.ylabel('Irradiance (mW/cm^2)')
plt.title('Irradiance vs Time')#
# plt.savefig('Color plot', bbox_inches='tight')
plt.show()
