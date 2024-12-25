# -*- coding: utf-8 -*-
"""
Created on Mon May 27 23:59:15 2024

@author: rossoneri
"""

import numpy as np
import matplotlib.pyplot as plt
X=np.loadtxt('./inDrop1.txt')
lmean=[]
lvar=[]
plt.figure()
for i in range(len(X[0])):
    lmean.append(np.average(X[:,i]))
    lvar.append(np.var(X[:,i]))
plt.scatter(lmean, lvar, s=0.2,c='b')
plt.xlim(0,50)
plt.ylim(0,50)
lx=np.linspace(0, 10,1000)
ly=lx
plt.scatter(lx, ly, s=0.5,c='r')
plt.show()
X=np.loadtxt("inDrop1_cp10k.txt")

lmean=[]
lvar=[]
plt.figure()
for i in range(len(X[0])):
    lmean.append(np.average(X[:,i]))
    lvar.append(np.var(X[:,i]))
plt.scatter(lmean, lvar, s=0.2,c='b')
plt.xlim(0,5)
plt.ylim(0,5)
lx=np.linspace(0, 10,1000)
ly=lx
plt.scatter(lx, ly, s=0.5,c='r')
plt.show()
X=np.loadtxt("inDrop1_cp10k&log.txt")
lmean=[]
lvar=[]
plt.figure()
for i in range(len(X[0])):
    lmean.append(np.average(X[:,i]))
    lvar.append(np.var(X[:,i]))
plt.scatter(lmean, lvar, s=0.2,c='b')
lx=np.linspace(0, 3,1000)
ly=lx
plt.scatter(lx, ly, s=0.5,c='r')
plt.show()

