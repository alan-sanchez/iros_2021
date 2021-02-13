#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

ir = [15.97, 14.30, 12.49, 10.63, 10.07, 10.41, 10.29, 9.45, 7.32, 4.46, 3.11, 2.35, 1.72, 1.37, 1.12, 0.91, 0.74,
        0.61, 0.52,  0.44,  0.38,  0.35,  0.32,  0.30, 0.29, 0.27, 0.27, 0.27, 0.26, 0.25, 0.24, 0.14, 0.23, 0.22]
x = np.linspace(0,16, len(ir))

# a,b,c,d,e = np.poly1d(np.polyfit(x, ir, 4))
mymodel = np.poly1d(np.polyfit(x, ir, 15))
print(type(mymodel))
myline = np.linspace(0,16,100)
best_fit = mymodel(myline)

# def test(x,a,b,c):
#     return a*x**2 + b*x + c
#
# popt, _ = curve_fit(test,x, ir)
# a,b,c = popt
#
# plt.scatter(x,ir)
#
# # define a sequence of inputs between the smallest and largest known inputs
# x_line = np.arange(min(x), max(x), 1)
# # calculate the output for the range
# y_line = test(x_line, a, b, c)
# # create a line plot for the mapping function
# plt.plot(x_line, y_line, '--', color='red')

plt.plot(x, ir)
plt.plot(myline, best_fit, '--', color = 'red')
plt.xlabel('Distance from the Center of Lit Surface (cm)')
plt.ylabel('Irradiance (mW/cm^2)')
plt.title('Distance vs Irradiance')
# plt.savefig("Distance_vs_Irradiance.png", bbox_inches='tight')
plt.show()
