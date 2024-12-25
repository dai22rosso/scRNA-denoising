# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 18:13:14 2024

@author: rossoneri
"""

import numpy as np
import anndata as ad
import sympy as sp
import pandas as pd
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from scipy.sparse import csr_matrix
from scipy.sparse import coo_matrix
# adata=ad.read_h5ad('./pancreas.h5ad')
# adata.X.todense()#将稀疏矩阵转成普通矩阵
# X=pd.DataFrame(adata.X.todense())
# cell_name=adata.obs.index
# print('cell',cell_name,len(cell_name))
# chr_name=adata.var.index
# print('chr',chr_name,len(chr_name))
# print(X)
# X=X.T
# U,S,Vt=np.linalg.svd(X)

with open('./S.txt','r') as f:
    data=f.readlines()
d=[]
for i in range(len(data)):
    d.append(float(data[i][:-2]))
d=np.array(d)
variances= d**2
real_rate=0
dimension=0
tol=np.sum(variances)
print(tol)
for i in range(10000):
    real_rate+=variances[i]/tol
    print(real_rate)
    if(real_rate>=0.60):
        print(i)
        dimension=i
        break
    else:
        continue
print(dimension)


    