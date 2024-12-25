import numpy as np
import anndata as ad
import pandas as pd
import matplotlib.pyplot as plt
import umap
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler

# def pca(X,k):
#     U_new=U[:,:(k-1)]
#     data=(np.transpose(U_new)@X.T)
#     return data
adata=ad.read_h5ad('./pancreas.h5ad')
adata.X.todense()
X=pd.DataFrame(adata.X.todense())
mat=X.to_numpy()
fname="./lower_dimension_data/UMAP_withstandard="
scaler = StandardScaler()
mat = StandardScaler().fit_transform(mat)

for i in range(3,4):
    for j in range(5):
        dist=(1/5)**j
        nbor=5**i*30
        umap_model = umap.UMAP(n_neighbors=nbor, min_dist=dist, n_components=2)
        umap_mat = umap_model.fit_transform(mat)
        fname1=fname+"dist="+str(dist)+"nbor_amount="+str(nbor)+"dim=2.txt"
        np.savetxt(fname1, umap_mat)
for i in range(4):
    for j in range(5):
        dist=(1/5)**j
        nbor=5**i*30
        umap_model = umap.UMAP(n_neighbors=nbor, min_dist=dist, n_components=3)
        umap_mat = umap_model.fit_transform(mat)
        fname1=fname+"dist="+str(dist)+"nbor_amount="+str(nbor)+"dim=3.txt"
        np.savetxt(fname1, umap_mat)
        



