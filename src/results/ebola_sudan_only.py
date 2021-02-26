import matplotlib.pyplot as plt
import csv

sensor_7 = []
with open('ebola_sudan.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        dosage = row
        sensor_7.append(float(dosage[7]))

test_list=[]
for i in range(0, len(dosage)):
    test_list.append(float(dosage[i]))


res = [sensor_7[i + 1] - sensor_7[i] for i in range(len(sensor_7)-1)]
s7 =  res[85:122]#[103:138]#[i for i in res if i != 0]
time = []
for i in range(len(s7)):
    time.append(i*.015)

# print(test_list)

Sensors = ['S0', 'S1', 'S2', 'S3', 'S4',
           'S5', 'S6', 'S7', 'S8', 'S9',
           'S10', 'S11', 'S12', 'S13', 'S14'
            ]
# plt.figure(0)
plt.bar(Sensors, test_list, alpha =0.5, yerr = 5, ecolor='black', capsize=2)
plt.axhline(y=27, color = 'b', linestyle='--')
plt.legend(['Required UV Dose for D90'])
plt.ylabel('UV Dosage (J/m^2)')
plt.xlabel('Array of UV sensors')
plt.title('Ebola Sudan Virus, k = 0.0867 m^2/J at D90')
plt.savefig("ebola_sudan_d90.png", bbox_inches='tight')


# plt.figure(1)
# plt.grid(linestyle='--')
# plt.xlabel('Time (sec)')
# plt.ylabel('Irradiance (W/m^2)')
# plt.errorbar(time, res[85:122], yerr = .1, capsize = 2, ecolor='black')
# plt.title('Time vs Measured Irradiance at Sensor 7')
# plt.savefig("ebola_sudan_s7.png", bbox_inches='tight')
plt.show()


#
# fig, (ax1, ax2) = plt.subplots(2)
# fig.tight_layout()
# # plt.subplots(1)
# ax1.bar(Sensors, test_list, alpha =0.5, yerr = 5, ecolor='black', capsize=2)
# ax1.axhline(y=26, color = 'b', linestyle='--')
# ax1.legend(['Required UV Dose for D90'])
# ax1.set_ylabel('UV Dosage (J/m^2)')
# ax1.set_xlabel('Array of UV sensors')
# ax1.set_title('Ebola Sudan Virus, k = 0.0867 m^2/J at D90')
# # ax1.savefig("ebola_sudan_d90.png", bbox_inches='tight')
#
#
# # plt.figure(1)
# # plt.subplots(1)
# ax2.grid(linestyle='--')
# ax2.set_xlabel('Exposure Time (sec)')
# ax2.set_ylabel('Irradiance (W/m^2)')
# ax2.errorbar(time, s7, yerr = .1, capsize = 2, ecolor='black')
# plt.legend(['Measured Irradiance at Sensor 7'])
# # ax2.set_title('Time vs Measured Irradiance at Sensor 7.')
# # ax2.savefig("ebola_sudan_s7.png", bbox_inches='tight')
# plt.show()
