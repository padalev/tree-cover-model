import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import ode

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

def r(P):
    return P/(h_P + P)*r_m
def dTdt(P,T):
    return P/(h_P + P)*r_m*T*(1-T/K)-m_A*T*h_A/(T + h_A) - m_f*T*h_f**p/(h_f**p + T**p)
def dPdt(P,T):
    return r_P*((P + b*T/K) - P)

T = np.linspace(-1,90,1000)
plt.plot(T,dTdt(3.5,T))
plt.grid()
plt.show()
