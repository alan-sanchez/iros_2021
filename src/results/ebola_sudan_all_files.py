import matplotlib.pyplot as plt
import csv
import numpy as np

csv_list = ['D90.csv','D999.csv','D99999.csv' ]#['ebola_sudan.csv', 'ebola_sudan_d999.csv',  'ebola_sudan_d99999.csv']
dosages = np.empty([5,15])
error = []
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
    error.append(np.std(test_list))


Sensors = ['S0', 'S1', 'S2', 'S3', 'S4',
           'S5', 'S6', 'S7', 'S8', 'S9',
           'S10', 'S11', 'S12', 'S13', 'S14'
            ]

X = np.arange(15)
# plt.add_axes([0,0,1,1])
# plt.bar(X - 0.50, dosages[0], alpha =0.5, yerr = 10, ecolor='black', capsize=2, width = 0.25)
# plt.bar(X - 0.25, dosages[1], alpha =0.5, yerr = 10, ecolor='black', capsize=2, width = 0.25)
# plt.bar(X + 0.00, dosages[2], alpha =0.5, yerr = 10, ecolor='black', capsize=2, width = 0.25)
# plt.bar(X + 0.25, dosages[3], alpha =0.5, yerr = 10, ecolor='black', capsize=2, width = 0.25)
# plt.bar(X + 0.50, dosages[4], alpha =0.5, yerr = 10, ecolor='black', capsize=2, width = 0.25)

# plt.add_axes([0,0,1,1])
plt.bar(X + 0.00, dosages[0], alpha =0.5, yerr = error[0], ecolor='black', capsize=2, width = 0.25)
plt.bar(X + 0.25, dosages[1], alpha =0.5, yerr = error[1], ecolor='black', capsize=2,color = 'r', width = 0.25)
plt.bar(X + 0.50, dosages[2], alpha =0.5, yerr = error[2], ecolor='black', capsize=2, color = 'g' ,width = 0.25)
plt.axhline(y=26.5, color = 'b', linestyle='--')
plt.axhline(y=79, color = 'r', linestyle='--')
plt.axhline(y=133, color = 'g', linestyle='--')

plt.legend(['Required UV Dose at $D_{90}$', 'Required UV Dose at $D_{99.9}$', 'Required UV Dose at $D_{99.999}$'])#,fontsize=12)
plt.title('Ebola Sudan, $k$ = 0.0867 $m^2/J$ at $D_{90}$, $D_{99.9}$, and $D_{99.999}$',fontsize=14)
plt.subplots_adjust(left = 0.11, bottom = 0.10, right = 0.89, top =0.93)

plt.xticks([r + 0.25 for r in range(len(Sensors))], Sensors)
plt.ylabel('UV Dosage ($J/m^2$)',fontsize=14)
plt.xlabel('Array of UV sensors',fontsize=14)
plt.savefig("ebola_diff_dvalues.png", bbox_inches='tight')

plt.show()
