
import numpy as np
import matplotlib.pyplot as plt
#This file is for the tool of mean and variance

#This function is to get the mean and variance of each gene
#return the list of mean and variance
def get_mean_var(X):
    lmean=[]
    lvar=[]
    for i in range(len(X[0])):
        lmean.append(np.average(X[:,i]))
        lvar.append(np.var(X[:,i]))
    return lmean, lvar
#This function is to show the mean and variance of each gene in 1 figure
def show_mean_var(X,xlim=10,s1=0.2,s2=0.5):
    lmean,lvar=get_mean_var(X)
    plt.scatter(lmean, lvar, s=s1,c='b')
    lx=np.linspace(0, xlim,1000)
    ly=lx
    plt.scatter(lx, ly, s=s2,c='r')
    plt.xlim(0,xlim)
    plt.ylim(0,xlim)
    plt.show()
# X=np.loadtxt('./pancreas_raw.txt')
# lmean=[]
# lvar=[]
# plt.figure()
# for i in range(len(X[0])):
#     lmean.append(np.average(X[:,i]))
#     lvar.append(np.var(X[:,i]))
# plt.scatter(lmean, lvar, s=0.2,c='b')
# lx=np.linspace(0, 10,1000)
# ly=lx
# plt.scatter(lx, ly, s=0.5,c='r')
# plt.xlim(0,50)
# plt.ylim(0,50)
# plt.show()
# X=np.loadtxt('./pancreas_normalized_sqrt_cp10k.txt')
# lmean=[]
# lvar=[]
# plt.figure()
# for i in range(len(X[0])):
#     lmean.append(np.average(X[:,i]))
#     lvar.append(np.var(X[:,i]))
# plt.scatter(lmean, lvar, s=0.2,c='b')
# plt.xlim(0,5)
# plt.ylim(0,5)
# lx=np.linspace(0, 10,1000)
# ly=lx
# plt.scatter(lx, ly, s=0.5,c='r')
# plt.show()
# X=np.loadtxt('./pancreas_normalized_log_cp10k_hvg.txt')
# lmean=[]
# lvar=[]
# plt.figure()
# for i in range(len(X[0])):
#     lmean.append(np.average(X[:,i]))
#     lvar.append(np.var(X[:,i]))
# plt.scatter(lmean, lvar, s=0.2,c='b')
# lx=np.linspace(0, 10,1000)
# ly=lx
# plt.scatter(lx, ly, s=0.5,c='r')
# plt.show()
# X=np.loadtxt('./pancreas_normalized_log_cp10k.txt')
# lmean=[]
# lvar=[]
# plt.figure()
# for i in range(len(X[0])):
#     lmean.append(np.average(X[:,i]))
#     lvar.append(np.var(X[:,i]))
# plt.scatter(lmean, lvar, s=0.2,c='b')
# lx=np.linspace(0, 10,1000)
# ly=lx
# plt.scatter(lx, ly, s=0.5,c='r')
# plt.show()
# X=np.loadtxt('./pancreas_normalized_cp10k.txt')
# lmean=[]
# lvar=[]
# plt.figure()
# for i in range(len(X[0])):
#     lmean.append(np.average(X[:,i]))
#     lvar.append(np.var(X[:,i]))
# plt.scatter(lmean, lvar, s=0.2,c='b')
# plt.xlim(0,50)
# plt.ylim(0,0.05)
# lx=np.linspace(0, 10,1000)
# ly=lx
# plt.scatter(lx, ly, s=0.5,c='r')
# plt.show()