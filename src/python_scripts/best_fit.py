#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def fit(order = 2, plotter = False):
    # Measured Irradaicne values
    ir = [15.97, 14.30, 12.49, 10.63, 10.07, 10.41, 10.29, 9.45, 7.32, 4.46, 3.11, 2.35, 1.72, 1.37, 1.12, 0.91, 0.74,
            0.61, 0.52,  0.44,  0.38,  0.35,  0.32,  0.30, 0.29, 0.27, 0.27, 0.27, 0.26, 0.25, 0.24, 0.14]#, 0.23, 0.22]

    # Meter positions from the center of the lit surface. stopped at 16cm
    x = np.linspace(0,15, len(ir))

    # Polyfit for data.
    model = np.poly1d(np.polyfit(x, ir, order))

    # Create a sequence of values to plug in the model
    x_line = np.linspace(0,15,100)

    # Input of x_line of data
    best_fit = model(x_line)

    if plotter:
        # Plot both original data and best fit
        plt.plot(x, ir)
        plt.plot(x_line, best_fit, '--', color = 'red')
        plt.xlabel('Distance from the Center of Lit Surface (cm)')
        plt.ylabel('Irradiance (mW/cm^2)')
        plt.title('10 W UV Flashlight held 40cm above UV meter')
        plt.legend(['Data', 'Best Fit'])
        # plt.savefig("Distance_vs_Irradiance.png", bbox_inches='tight')
        plt.show()

    return model

if __name__ == '__main__':
    model = fit(15, True)
    print(model)
