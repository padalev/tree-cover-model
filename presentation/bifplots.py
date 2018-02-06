import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Wedge
from matplotlib.patches import Circle


def dx(x,r):
    return r + x**2

plt.figure(1)
x = np.linspace(-1.5,1.5,1000)
plt.plot(x,dx(x,-1),'k',zorder=2)
plt.plot((-1.25,-1.2,-1.25),(-0.05,0,0.05),'k',zorder=2)
plt.plot((-0.75,-0.8,-0.75),(-0.05,0,0.05),'k',zorder=2)
plt.plot((1.15,1.2,1.15),(-0.05,0,0.05),'k',zorder=2)
plt.plot((0.85,0.8,0.85),(-0.05,0,0.05),'k',zorder=2)
plt.axis('off')
ax = plt.gca()
plt.axhline(0, color='grey',zorder=1)
plt.axvline(0, color='grey',zorder=1)
w1 = Circle([1,0], 0.04, fc='w', lw=1, ec='k',zorder=3)
w2 = Circle([-1,0], 0.04, fc='k', lw=1, ec='k',zorder=3)
for wedge in [w1, w2]:
        ax.add_artist(wedge)
plt.savefig('fig1.pdf')

plt.figure(2)
x = np.linspace(-1.5,1.5,1000)
plt.plot(x,dx(x,0),'k',zorder=2)
plt.axis('off')
ax = plt.gca()
plt.axhline(0, color='grey',zorder=1)
plt.axvline(0, color='grey',zorder=1)
plt.plot((-1.05,-1,-1.05),(-0.05,0,0.05),'k',zorder=2)
plt.plot((0.95,1,0.95),(-0.05,0,0.05),'k',zorder=2)
w1 = Wedge([0,0], 0.04, -90, 90, fc='w', lw=1, ec='k',zorder=3)
w2 = Wedge([0,0], 0.04, 90, 270, fc='k', lw=1, ec='k',zorder=3)
for wedge in [w1, w2]:
        ax.add_artist(wedge)
plt.savefig('fig2.pdf')

plt.figure(3)
x = np.linspace(-1.5,1.5,1000)
plt.plot(x,dx(x,1),'k',zorder=2)
plt.plot((-1.05,-1,-1.05),(-0.05,0,0.05),'k',zorder=2)
plt.plot((0.95,1,0.95),(-0.05,0,0.05),'k',zorder=2)
plt.axis('off')
plt.axhline(0, color='grey',zorder=1)
plt.axvline(0, color='grey',zorder=1)
plt.savefig('fig3.pdf')


plt.show()
