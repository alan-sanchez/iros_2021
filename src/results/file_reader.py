import matplotlib.pyplot as plt
import csv

with open('ebola_sudan_d99.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        dosage = row

test_list=[]
for i in range(0, len(dosage)):
    test_list.append(float(dosage[i]))

Sensors = ['S0', 'S1', 'S2', 'S3', 'S4',
           'S5', 'S6', 'S7', 'S8', 'S9',
           'S10', 'S11', 'S12', 'S13', 'S14'
            ]

plt.bar(Sensors, test_list, alpha =0.5, yerr = 10, ecolor='black', capsize=2)

plt.show()
print(test_list)
