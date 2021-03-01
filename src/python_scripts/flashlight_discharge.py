#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt

# np array of 10 seconds for 3 minutes.
# x = np.linspace(0,240,25)
# Append larger times. Also convert to mins
# x = np.append(x, [[300, 600, 900, 1200, 1500, 1800]])/60
x = [0, 5, 10, 15, 20, 25, 30]


# # Irradiance of flashlight with battery connected to charger. Trial #1
# ir_battery_with_charger_1 = [21.32, 20.67, 20.44, 20.35, 20.22, 20.11, 20.01, 19.93, 19.85, 19.76, 19.70, 19.63,
#                              19.56, 19.51, 19.45, 19.39, 19.33, 19.27, 19.22, 19.17, 19.13, 19.08, 19.02, 18.97,
#                              18.92, 18.61, 17.38, 16.53, 15.92, 15.42, 14.95]
#
# # Irradiance of flashlight with battery connected to charger. Trial #2
# ir_battery_with_charger_2 = [20.65, 20.33, 20.24, 20.12, 20.04, 19.94, 19.86, 19.79, 19.70, 19.64, 19.58, 19.51,
#                              19.44, 19.38, 19.32, 19.25, 19.19, 19.14, 19.08, 19.02, 18.97, 18.93, 18.87, 18.82,
#                              18.77, 18.49, 17.26, 16.44, 15.97, 15.50, 15.12]
#
# # Irradiance of flashlight with only battery.
# ir_battery = [17.05, 16.75, 16.56, 16.43, 16.32, 16.21, 16.13, 16.05, 15.97, 15.91, 15.84, 15.77,
#               15.71, 15.65, 15.60, 15.54, 15.49, 15.43, 15.38, 15.34, 15.29, 15.24, 15.20, 15.15,
#               15.10, 14.85, 13.78, 12.89, 12.26, 11.73, 11.19]

# Irradiance of flashlight with no battery and connected to charger.
ir_charger = [17.80, 17.79, 17.79, 17.76, 17.76, 17.75, 17.73, 17.67, 17.64, 17.58, 17.52,
              17.47, 17.40, 17.38, 17.30, 17.25, 17.20, 17.13, 17.08, 17.03, 16.99, 16.93,
              16.89, 16.83, 16.78, 16.52, 15.34, 14.67, 14.26, 13.96, 13.80]#, 13.74,
              # 13.71, 13.68, 13.61]

ir_charger_smaller = [17.80,  16.52, 15.34, 14.67, 14.26, 13.96, 13.80 ]

#x_new = np.append(x, [[35, 40, 45, 50]])

# Plot all measured data
# plt.plot(x,ir_battery_with_charger_1)
# plt.plot(x,ir_battery_with_charger_2, 'r')
# plt.plot(x,ir_battery, 'k')
# plt.plot(x,ir_charger)


plt.grid(linestyle='--')

plt.xlabel('Exposure Time ($min$)',fontsize=14)
plt.ylabel('Irradiance ($mW/cm^2$)',fontsize=14)
plt.title('UV Flashlight Discharge',fontsize=16)
plt.errorbar(x, ir_charger_smaller, linewidth=2.5 ,yerr = .1, capsize = 3, ecolor='black',zorder=1 )

# plt.legend(['Battery & Charger #1', 'Battery & Charger #2', 'Battery Only', 'Charger Only'])
plt.savefig('flashlight_discharge.png', bbox_inches='tight')
plt.show()
