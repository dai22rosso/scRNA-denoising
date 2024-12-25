# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 17:57:02 2024

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
X=X.T
pca=PCA(n_components=200)
newX=pca.fit_transform(X)
# K=get_K(newX)
K_re=KMeans(n_clusters=10,random_state=9).fit_predict(X)
plt.scatter(X[:,0], X[:,1], K_re)
plt.show()

