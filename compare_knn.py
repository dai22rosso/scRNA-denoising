import numpy as np
import time
from dist_utils import *
from knn_utils import *
Dis=np.loadtxt('norm_for_loop.txt',dtype=int)
k=10
neighbor=numpy_argsort(Dis,k)
np.savetxt('numpy_argsort1.txt',neighbor,fmt='%d')
neighbor=sklearn_knn(Dis,k)
np.savetxt('sklearn_knn1.txt',neighbor,fmt='%d')
neighbor=kdtree_knn(Dis,k)
np.savetxt('kdtree_knn1.txt',neighbor,fmt='%d')
neighbor=balltree_knn(Dis,k)
np.savetxt('balltree_knn1.txt',neighbor,fmt='%d')
k=20
neighbor=numpy_argsort(Dis,k)
np.savetxt('numpy_argsort2.txt',neighbor,fmt='%d')

neighbor=sklearn_knn(Dis,k)
np.savetxt('sklearn_knn2.txt',neighbor,fmt='%d')
neighbor=kdtree_knn(Dis,k)
np.savetxt('kdtree_knn2.txt',neighbor,fmt='%d')
neighbor=balltree_knn(Dis,k)
np.savetxt('balltree_knn2.txt',neighbor,fmt='%d')

