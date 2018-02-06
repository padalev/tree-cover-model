import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import ode
from scipy import optimize
from matplotlib.patches import Wedge
from matplotlib.patches import Circle

h_A = 10
h_f = 64
h_P = 0.5
K = 90
m_A = 0.15
m_f = 0.11
p = 7
b = 0
r_m = 0.3
r_P = 1

def dTdt0(T,P):
    return P/(h_P + P)*r_m*T*(1-T/K)
def dTdt1(T,P):
    return -m_A*T*h_A/(T + h_A)
def dTdt2(T,P):
    return - m_f*T*h_f**p/(h_f**p + T**p)
def dTdt(T,P):
    return P/(h_P + P)*r_m*T*(1-T/K)-m_A*T*h_A/(T + h_A) - m_f*T*h_f**p/(h_f**p + T**p)

plt.figure(1)
T = np.linspace(-2,80,1000)
plt.plot(T,dTdt(T,1.5),'k-',zorder=2)
#plt.plot(T,dTdt0(T,3.5),'k--',zorder=2)
#plt.plot(T,dTdt1(T,3.5),'k-.',zorder=2)
#plt.plot(T,dTdt2(T,3.5),'k:',zorder=2)
plt.axhline(0, color='grey',zorder=1)
plt.axvline(0, color='grey',zorder=1)
plt.xlim(-2,80)
plt.xlabel(r'Tree Cover in %')
plt.ylabel(r'Growth rate in % / yr$^{-1}$')
plt.savefig('eqfig4.pdf')


plt.show()
