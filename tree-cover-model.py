import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import ode
from scipy import optimize

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
def dTdt(T,P):
    return P/(h_P + P)*r_m*T*(1-T/K)-m_A*T*h_A/(T + h_A) - m_f*T*h_f**p/(h_f**p + T**p)
def dPdt(P,T):
    return r_P*((P + b*T/K) - P)


#plt.figure(1)
#T = np.linspace(1,100,1000)
#plt.plot(T,dTdt(T,1.5))
#plt.grid()


maxNumSolutions = 5
precipitationvalues = 100000
Tvalues = 1000
solutionsPstable = []
solutionsTstable = []
solutionsPunstable = []
solutionsTunstable = []

precipitation = np.linspace(0,5,precipitationvalues)

def zeroSolutions(pre):
    def dTdtrun(x):
        P = pre
        return dTdt(x,P)
    zeropointsT = []
    zeropointsP = []
    T = np.linspace(-1,101,Tvalues)
    dt_ = dTdt(T,pre)
    dt = dt_**2
    for k in range(Tvalues-2):
        if ( dt[k+1] < dt[k] ):
            if ( dt[k+1] < dt[k+2] ):
                if ( dt_[k] < 0 and dt_[k+2] > 0 ) or ( dt_[k] > 0 and dt_[k+2] < 0 ):
                    zeropointsT.append( optimize.newton( dTdtrun, T[k], maxiter=30 ) )
                    zeropointsP.append( pre )
    return zeropointsP, zeropointsT

def sortType(solutionsP, solutionsT):
    zeropointsTstable = []
    zeropointsPstable = []
    zeropointsTunstable = []
    zeropointsPunstable = []
    for precounter, pre in enumerate(solutionsP):
        if ( dTdt(solutionsT[precounter],pre) < 0 and dTdt(solutionsT[precounter]+0.1,pre) > 0 ):
            zeropointsTunstable.append( solutionsT[precounter] )
            zeropointsPunstable.append( pre )
        if ( dTdt(solutionsT[precounter],pre) > 0 and dTdt(solutionsT[precounter]+0.1,pre) < 0 ):
            zeropointsTstable.append( solutionsT[precounter] )
            zeropointsPstable.append( pre )
    zeropointsTstable,zeropointsPstable = zip(*sorted(zip(zeropointsTstable,zeropointsPstable)))
    zeropointsTunstable,zeropointsPunstable = zip(*sorted(zip(zeropointsTunstable,zeropointsPunstable)))
    return zeropointsTunstable, zeropointsPunstable, zeropointsTstable, zeropointsPstable

def plotnsort(zeropointsTunstable, zeropointsPunstable, zeropointsTstable, zeropointsPstable):
    tempP = []
    tempT = []
    for precounter, pre in enumerate(zeropointsPstable):
        if (len(zeropointsPstable) > precounter+1):
            if np.absolute(zeropointsTstable[precounter] - zeropointsTstable[precounter+1]) > 1:
                tempP.append(pre)
                tempT.append(zeropointsTstable[precounter])
                tempP,tempT = zip(*sorted(zip(tempP,tempT)))
                plt.plot(tempP,tempT,'k-')
                tempP = []
                tempT = []
            else:
                tempP.append(pre)
                tempT.append(zeropointsTstable[precounter])
    tempP,tempT = zip(*sorted(zip(tempP,tempT)))
    plt.plot(tempP,tempT,'k-')
    tempP = []
    tempT = []
    for precounter, pre in enumerate(zeropointsPunstable):
        if (len(zeropointsPunstable) > precounter+1):
            if np.absolute(zeropointsTunstable[precounter] - zeropointsTunstable[precounter+1]) > 1:
                tempP.append(pre)
                tempT.append(zeropointsTunstable[precounter])
                tempP,tempT = zip(*sorted(zip(tempP,tempT)))
                plt.plot(tempP,tempT,'k--')
                tempP = []
                tempT = []
            else:
                tempP.append(pre)
                tempT.append(zeropointsTunstable[precounter])
    tempP,tempT = zip(*sorted(zip(tempP,tempT)))
    plt.plot(tempP,tempT,'k--')


solutionsP = []
solutionsT = []
for precounter, pre in enumerate(precipitation):
    print(pre)
    zeropointsP, zeropointsT = zeroSolutions(pre)
    solutionsP.extend(zeropointsP)
    solutionsT.extend(zeropointsT)

solutionsTunstable, solutionsPunstable, solutionsTstable, solutionsPstable = sortType(solutionsP, solutionsT)
#print "Die Antwort lautet: " + str(solutions)
#solutionsT,solutionsP = zip(*sorted(zip(solutionsT,solutionsP)))
plt.figure(2)
plotnsort(solutionsTunstable, solutionsPunstable, solutionsTstable, solutionsPstable)
plt.grid()
plt.xlabel(r'Precipitation in mm yr$^{-1}$')
plt.ylabel(r'Tree Cover in %')

plt.savefig('final.pdf')

plt.show()
