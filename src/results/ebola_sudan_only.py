import matplotlib.pyplot as plt
import numpy as np
import csv

sensor_7 = []
sensor_10 = []
with open('D90.csv', 'r') as file: #ebola_sudan.csv
    reader = csv.reader(file)
    for row in reader:
        dosage = row
        sensor_7.append(float(dosage[7]))
        sensor_10.append(float(dosage[10]))


test_list=[]
for i in range(0, len(dosage)):
    test_list.append(float(dosage[i]))

mean = np.mean(test_list)
std = np.std(test_list)


res = [sensor_7[i + 1] - sensor_7[i] for i in range(len(sensor_7)-1)]
# res = [sensor_10[i + 1] - sensor_10[i] for i in range(len(sensor_10)-1)]

s =  res[121:168]#[i for i in res if i != 0]#
time=[]
for i in range(len(s)):
    time.append(i*.015)



# propagation error is .15 percent
y_prop = 0.15

# print(test_list)

Sensors = ['S0', 'S1', 'S2', 'S3', 'S4',
           'S5', 'S6', 'S7', 'S8', 'S9',
           'S10', 'S11', 'S12', 'S13', 'S14'
            ]
plt.figure(0)
plt.bar(Sensors, test_list, alpha =0.5, yerr = std, ecolor='black', capsize=2)
plt.axhline(y=27, color = 'b', linestyle='--')
plt.legend(['Required UV Dose for $D_{90}$'], fontsize=12)
plt.ylabel('UV Dosage ($J/m^2$)', fontsize=14)
plt.xlabel('Array of UV sensors', fontsize=14)
plt.title('Ebola Sudan, $k$ = 0.0867 $m^2/J$ at $D_{90}$', fontsize=16)
plt.savefig("ebola_sudan_d90.png", bbox_inches='tight')
#

# plt.figure(1)
# plt.grid(linestyle='--')
# plt.xlabel('Time ($s$)', fontsize=14)
# plt.ylabel('Irradiance ($W/m^2$)', fontsize=14)
# plt.errorbar(time, s, yerr = y_prop, capsize = 2, ecolor='black')
# plt.title('Time vs Measured Irradiance at Sensor 7',fontsize=16)
# plt.savefig("ebola_sudan_s7.png", bbox_inches='tight')
plt.show()
