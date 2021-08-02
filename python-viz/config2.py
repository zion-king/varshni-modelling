# Configuration 1: Low Perturbation of a on V

# Load dependencies
import pandas as pd
import numpy as np
from random import * 
from scipy.interpolate import make_interp_spline,BSpline
import matplotlib.pyplot as plt
%matplotlib inline

# Import data for Case 2
case2 = pd.read_csv('config2.csv', header = None) 

#Drop missing values
case2.drop([0],inplace = True)
case2.dropna(axis=1,inplace = True) 

# Plot r against initial and modified potentials
r = np.linspace(case2[1].min(),case2[1].max(),300)
spline1 = make_interp_spline(case2[1],case2[2],k=3)
spline2 = make_interp_spline(case2[1],case2[3],k=3)
V1 = spline1(r)
V2 = spline2(r)
plt.plot(r,V1,'b',r,V2,'r--',linewidth=1.2)
l = plt.legend(['Initial','Perturbed'],loc=9)
plt.setp(l.texts, family = 'Baskerville Old Face')
plt.xlabel('r',fontname = 'Cambria')
plt.ylabel('Potential', fontname = 'Cambria') 

a = 0.15
alpha = 0.15
dV = (a-case1[2])*(alpha+1/case1[1])
dV1 = np.linspace(dV.min(),dV.max(),300)
spline1 = make_interp_spline(dV.sort_values(),case1[2],k=3)
V1smooth = spline1(dV1)
a_mod = 0.15 + 0.4*random()
dVnew = (a_mod-case1[2])*(alpha+1/case1[1])
dV2 = np.linspace(dVnew.min(),dVnew.max(),300)
spline2 = make_interp_spline(dVnew.sort_values(),case1[3],k=3)
V2smooth = spline2(dV2)
plt.plot(V1smooth,dV1,'b',V2smooth,dV2,'r--',linewidth=1.2)
l = plt.legend(['Initial','Perturbed'],loc=6)
plt.setp(l.texts, family = 'Baskerville Old Face')
plt.xlabel('Potential',fontname = 'Cambria')
plt.ylabel('dV/dr', fontname = 'Cambria') 

a = 0.5
alpha = 0.15
dV = (a-case1[2])*(alpha+1/case1[1])
dV1 = np.linspace(dV.min(),dV.max(),300)
spline1 = make_interp_spline(dV.sort_values(),case1[2],k=3)
V1smooth = spline1(dV1)
a_mod = 0.5 + 0.4*random()
dVnew = (a_mod-case1[2])*(alpha+1/case1[1])
dV2 = np.linspace(dVnew.min(),dVnew.max(),300)
spline2 = make_interp_spline(dVnew.sort_values(),case1[3],k=3)
V2smooth = spline2(dV2)
plt.plot(V1smooth,dV1,'b',V2smooth,dV2,'r--',linewidth=1.2)
l = plt.legend(['Initial','Perturbed'],loc=9)
plt.setp(l.texts, family = 'Baskerville Old Face')
plt.xlabel('Potential',fontname = 'Cambria')
plt.ylabel('dV/dr', fontname = 'Cambria')
