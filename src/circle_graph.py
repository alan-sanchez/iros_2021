#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb

x = np.linspace(-1,1,400)
y = np.linspace(-1,1,400)

x,y = np.meshgrid(x,y)

def f(a,b):
    r = np.sqrt(x**2 + y**2)

    return 125.8*r**4 - 329.5*r**3 + 318.8*r**2 - 141.4*r + 26.59

z =f(x,y)
# ax = sb.heatmap(z)
fig, ax = plt.subplots(1,1)
im = ax.imshow(z)
fig.colorbar(im)
im.set_label('yo')#,labelpad=-40, y=1.05, rotation=0)

# plt.xlim(-1.25,1.25)
# plt.ylim(-1.25,1.25)

plt.grid(linestyle='--')

plt.xlabel('Distance from the Center of Lit Surface (cm)')
plt.ylabel('Distance from the Center of Lit Surface (cm)')
plt.title('Distance vs Irradiance')#
plt.savefig('Color plot', bbox_inches='tight')
plt.show()
