import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np


def barlist(n):
    return my_data[n][:]

my_data = np.genfromtxt('ebola_sudan.csv', delimiter=',')
Sensors = ['S0', 'S1', 'S2', 'S3', 'S4',
           'S5', 'S6', 'S7', 'S8', 'S9',
           'S10', 'S11', 'S12', 'S13', 'S14'
            ]


r,c = my_data.shape

fig=plt.figure()



n=r-1 #Number of frames
x=range(c)
barcollection = plt.bar(Sensors,barlist(200))
plt.axhline(y=27, color = 'r', linestyle='--')
plt.legend(['Required UV Dose for D90'])
plt.ylabel('UV Dosage (J/m^2)')
plt.xlabel('Array of UV sensors')
plt.title('Ebola Sudan Virus, k = 0.0867 m^2/J at D90')

# print(type(barcollection))


def animate(i):
    y=barlist(i)
    for i in range(len(barcollection)):
        barcollection[i].set_height(y[i])

anim=animation.FuncAnimation(fig,animate,repeat=False,blit=False,frames=n,
                             interval=15)

anim.save('mymovie.mp4',writer=animation.FFMpegWriter(fps=32))
plt.show()
