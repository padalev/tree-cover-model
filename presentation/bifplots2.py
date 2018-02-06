import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import ode
from scipy import optimize


def x(r):
    return r

plt.figure(1)
r = np.linspace(-1.5,0,1000)
plt.plot(r,x(r),'k--',zorder=2)
plt.plot(r,np.zeros(1000),'k-',zorder=2)
r = np.linspace(0,1.5,1000)
plt.plot(r,np.zeros(1000),'k--',zorder=2)
plt.plot(r,x(r),'k-',zorder=2)
plt.axis('off')
ax = plt.gca()
plt.axhline(0, color='grey',zorder=1)
plt.axvline(0, color='grey',zorder=1)
plt.savefig('fig5.pdf')


plt.show()
