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


plt.figure(1)
T = np.linspace(1,100,1000)
plt.plot(T,dTdt(1.5,T))
plt.plot(T,dTdt(1.5,T)**2)
plt.grid()


maxNumSolutions = 5
precipitationvalues = 1000
Tvalues = 10000
solutions = np.zeros((precipitationvalues,maxNumSolutions))

precipitation = np.linspace(0,5,precipitationvalues)

for precounter, pre in enumerate(precipitation):
    solcounter = 0
    T = np.linspace(-1,101,Tvalues)
    dt_ = dTdt(pre,T)
    dt = dt_**2
    for k in range(Tvalues-2):
        if ( dt[k+1] < dt[k] ):
            if ( dt[k+1] < dt[k+2] ):
                if ( dt_[k] < 0 and dt_[k+2] > 0 ) or ( dt_[k] > 0 and dt_[k+2] < 0 ) :
                    solutions.itemset((precounter,solcounter), T[k])
                    solcounter = solcounter + 1

# ----- alternative Methode -----
# ----- funktioniert leider nicht so irre gut -----
#
# maxNumSolutions = 5
# precipitationvalues = 1000
# Tvalues = 10000
# altsolutions = np.zeros((precipitationvalues,maxNumSolutions))
#
# precipitation = np.linspace(0,5,precipitationvalues)
#
# for precounter, pre in enumerate(precipitation):
#     solcounter = 0
#     T = np.linspace(-1,101,Tvalues)
#     dt = dTdt(pre,T)
#     for k in range(Tvalues-1):
#         if( dt[k] > 0 ):
#             if( dt[k+1] < 0 ):
#                 altsolutions.itemset((precounter,solcounter), T[k])
#                 solcounter = solcounter + 1
#         elif( dt[k] < 0 ):
#             if( dt[k+1] > 0 ):
#                 altsolutions.itemset((precounter,solcounter), T[k])
#                 solcounter = solcounter + 1

solutions.sort(axis=1)
#print "Die Antwort lautet: " + str(solutions)
plt.figure(2)
plt.plot(precipitation,solutions)
plt.grid()

plt.show()
