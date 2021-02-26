import matplotlib.pyplot as plt
import csv
import numpy as np

csv_list = ['ebola_sudan.csv','Staph_aureus.csv', 'Ecoli.csv']
dosages = np.empty([5,15])
iter = 0

for e in csv_list:

    with open(e, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            dosage = row

    test_list = []
    for i in range(0, len(dosage)):
        test_list.append(float(dosage[i]))

    dosages[iter] = test_list
    iter = iter + 1



Sensors = ['S0', 'S1', 'S2', 'S3', 'S4',
           'S5', 'S6', 'S7', 'S8', 'S9',
           'S10', 'S11', 'S12', 'S13', 'S14'
            ]
# print dosages

X = np.arange(15)
# plt.add_axes([0,0,1,1])
plt.bar(X + 0.00, dosages[0], alpha =0.5, yerr = 5, ecolor='black', capsize=2, width = 0.25)
plt.bar(X + 0.25, dosages[1], alpha =0.5, yerr = 5, ecolor='black', capsize=2,color = 'r', width = 0.25)
plt.bar(X + 0.50, dosages[2], alpha =0.5, yerr = 5, ecolor='black', capsize=2, color = 'g' ,width = 0.25)
plt.axhline(y=27, color = 'b', linestyle='--')
plt.axhline(y=30, color = 'r', linestyle='--')
plt.axhline(y=34, color = 'g', linestyle='--')

plt.legend(['Required UV Dose for Ebola Sudan at D90', 'Required UV Dose for Staph. Aureus at D90', 'Required UV Dose for E.coli at D90'])
plt.title('Measured UV Dosage for Three Different Pathogens.')
plt.subplots_adjust(left = 0.09, bottom = 0.10, right = 0.99, top =0.93)

plt.xticks([r + 0.25 for r in range(len(Sensors))], Sensors)
plt.ylabel('UV Dosage (J/m^2)')
plt.xlabel('Array of UV sensors')
plt.savefig("three_different_virus.png", bbox_inches='tight')

plt.show()
