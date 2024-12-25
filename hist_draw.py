# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 23:06:10 2024

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
with open('./hist.txt','r') as f:
    data=f.readlines()
d=[]
print(d)

d=np.array(d)
d[0]=0

Gauss_filter()
plt.plot(d)
plt.show()
