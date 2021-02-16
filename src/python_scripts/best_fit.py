#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def fit(order = 2, plotter = False):
    ## Measured Irradiance values
    ## Iradiance value at .4 meters from UV sensor
    #ir = [15.97, 14.30, 12.49, 10.63, 10.07, 10.41, 10.29, 9.45, 7.32, 4.46, 3.11, 2.35, 1.72, 1.37, 1.12, 0.91, 0.74,
            # 0.61, 0.52,  0.44,  0.38,  0.35,  0.32,  0.30, 0.29, 0.27, 0.27, 0.27, 0.26, 0.25, 0.24, 0.14]#, 0.23, 0.22]

    ## Iradiance value at .3 meters from UV sensor. Trial #1
    # ir = [27.75, 26.29, 22.31, 17.82, 17.10, 17.22, 15.57, 10.74, 6.10, 3.88, 2.72, 2.02, 1.50, 1.13, .91, 0.76, 0.67, 0.61, 0.57,
    #       0.54, 0.52, 0.49, 0.48, 0.46, 0.44, 0.43, 0.42, 0.40, 0.39, 0.38, 0.36, 0.35, 0.33]

    # Iradiance value at .3 meters from UV sensor. Trial #2
    ir = [26.96,25.27, 21.61, 17.78, 16.46, 16.57, 15.11, 11.30, 6.53, 3.71, 2.62, 1.93, 1.44, 1.09, 0.89, 0.75, 0.66,
          0.59, 0.55, 0.52, 0.50, 0.48, 0.46, 0.44, 0.43, 0.42, 0.40, 0.39, 0.38, 0.37, 0.35, 0.34, 0.32]

    # Meter positions from the center of the lit surface. stopped at 16cm
    x = np.linspace(0,(len(ir)-1)/2, len(ir))

    # Polyfit for data.
    model = np.poly1d(np.polyfit(x, ir, order))

    # Create a sequence of values to plug in the model
    x_line = np.linspace(0,(len(ir)-1)/2,len(ir))

    # Input of x_line of data
    best_fit = model(x_line)

    if plotter:
        # Plot both original data and best fit. Only plotted data that went up to
        # 10 cm.
        plt.grid(linestyle='--')
        # plt.scatter(x, ir, xerr = .1)
        plt.errorbar(x[0:21], ir[0:21], xerr = .2, yerr = 1, fmt='o', capsize = 3)
        plt.plot(x_line[0:21], best_fit[0:21], '--', color = 'red')
        plt.xlabel('Distance from the Center of Lit Surface (cm)')
        plt.ylabel('Irradiance (mW/cm^2)')
        plt.title('10W UV Flashlight held 30cm above UV meter')
        plt.legend(['Best Fit', 'UV Meter Measurements'])
        plt.savefig("Distance_vs_Irradiance.png", bbox_inches='tight')
        plt.show()

    # This returns a polynomial function that takes single value or an array
    # as an input value. Ex: model(np.array([0,1,2,3]))
    return model

if __name__ == '__main__':
    model = fit(3, plotter = True)
    print(model)
