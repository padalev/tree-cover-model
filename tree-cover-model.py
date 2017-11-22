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
#plt.plot(T,dTdt(1.5,T)**2)
plt.grid()


maxNumSolutions = 5
precipitationvalues = 10000
Tvalues = 10000
solutionsPstable = []
solutionsTstable = []
solutionsPunstable = []
solutionsTunstable = []

precipitation = np.linspace(0,5,precipitationvalues)

def zeroSolutions(pre):
    zeropointsTstable = []
    zeropointsPstable = []
    zeropointsTunstable = []
    zeropointsPunstable = []
    T = np.linspace(-1,101,Tvalues)
    dt_ = dTdt(pre,T)
    dt = dt_**2
    for k in range(Tvalues-2):
        if ( dt[k+1] < dt[k] ):
            if ( dt[k+1] < dt[k+2] ):
                if ( dt_[k] < 0 and dt_[k+2] > 0 ):
                    zeropointsTunstable.append( T[k] )
                    zeropointsPunstable.append( pre )
                if ( dt_[k] > 0 and dt_[k+2] < 0 ):
                    zeropointsTstable.append( T[k] )
                    zeropointsPstable.append( pre )

    return zeropointsPstable, zeropointsTstable, zeropointsPunstable, zeropointsTunstable

for precounter, pre in enumerate(precipitation):
    print(pre)
    zeropointsPstable, zeropointsTstable, zeropointsPunstable, zeropointsTunstable = zeroSolutions(pre)
    solutionsPstable.extend(zeropointsPstable)
    solutionsTstable.extend(zeropointsTstable)
    solutionsPunstable.extend(zeropointsPunstable)
    solutionsTunstable.extend(zeropointsTunstable)


#print "Die Antwort lautet: " + str(solutions)
solutionsTstable,solutionsPstable = zip(*sorted(zip(solutionsTstable,solutionsPstable)))
solutionsTunstable,solutionsPunstable = zip(*sorted(zip(solutionsTunstable,solutionsPunstable)))
plt.figure(2)
plt.plot(solutionsPstable,solutionsTstable,'k-')
plt.plot(solutionsPunstable,solutionsTunstable,'k--')
plt.grid()

plt.show()
