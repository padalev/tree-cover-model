import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import ode
from scipy import optimize


def x(r):
    return (-r)**(1/2)

plt.figure(1)
r = np.linspace(-1,0,1000)
plt.plot(r,x(r),'k--',zorder=2)
plt.plot(r,-x(r),'k-',zorder=2)
plt.axis('off')
ax = plt.gca()
plt.axhline(0, color='grey',zorder=1)
plt.axvline(0, color='grey',zorder=1)
plt.xlim(-1.2,1.2)
plt.savefig('fig4.pdf')


plt.show()
