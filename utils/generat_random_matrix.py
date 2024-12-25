# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 22:35:43 2024

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
adata=ad.read_h5ad('./pancreas.h5ad')
adata.X.todense()#将稀疏矩阵转成普通矩阵
X=pd.DataFrame(adata.X.todense())
cell_name=adata.obs.index
print('cell',cell_name,len(cell_name))
chr_name=adata.var.index
print('chr',chr_name,len(chr_name))
print(X)
X=np.array(X.T)
l=[]
for i in range(len(X)):
    for ii in range(len(X[0])):
        if(X[i][ii]!=0):
            with open('./data.txt','a') as f:
                print(str(X[i][ii]),file=f)
        else:
            continue
