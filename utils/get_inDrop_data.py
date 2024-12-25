# -*- coding: utf-8 -*-
"""
Created on Wed May 22 05:42:55 2024

@author: rossoneri
"""

import numpy as np
import anndata as ad
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE

def find_elem(l,elem):
    for k in range(len(l)):
        if elem==l[k]:
            return True
    return False

# def pca(X,k):
#     U_new=U[:,:(k-1)]
#     data=(np.transpose(U_new)@X.T)
#     return data
adata=ad.read_h5ad('./pancreas.h5ad')

# k=6321
# k2=8528
# for i in range(10000):
#     if(l[k]!='inDrop1'):
#         break
#     else:
#         k+=1
# ls=adata[6321:8258].obs['celltype']
# count=np.zeros(14)
# elem=['acinar', 'beta', 'delta', 'activated_stellate', 'ductal', 'alpha', 'epsilon', 'gamma', 'endothelial', 'quiescent_stellate', 'macrophage', 'schwann', 'mast', 't_cell']
# for i in range(len(ls)):
#     count[elem.index(ls[i])]+=1
# print(count,elem)
keep_techs=['inDrop1']
adata1 = adata[adata.obs["tech"].isin(keep_techs)].copy()
adata1.X=adata[6321:8258].layers["counts"]
mat=np.array(adata1.X.todense())

np.savetxt("./inDrop1.txt", mat)