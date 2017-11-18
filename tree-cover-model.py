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

T = np.linspace(1,100,1000)
plt.plot(T,dTdt(3.5,T))
plt.grid()
plt.show()


maxNumSolutions = 10
pericipationvalues = 1000
Tvalues = 10000
solutions = np.zeros((pericipationvalues,maxNumSolutions))
percounter = 0

pericipation = np.linspace(0,5,pericipationvalues)
for per in pericipation:
    solcounter = 0
    T = np.linspace(-1,101,Tvalues)
    dt = dTdt(per,T)
    dt = dt**2
    for k in range(Tvalues-2):
        if((dt.item(k+1))<(dt.item(k))):
            if((dt.item(k+1))<(dt.item(k+2))):
                solutions.itemset((percounter,solcounter), T.item(k))
                solcounter = solcounter + 1
        
    percounter = percounter + 1
solutions.sort(axis=1)
print "Die Antwort lautet: " + str(solutions)
plt.plot(pericipation,solutions)
plt.grid()
plt.show()