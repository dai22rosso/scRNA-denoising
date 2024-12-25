import numpy as np
import scipy as sp
from scipy.spatial.distance import pdist
from scipy.spatial.distance import squareform
def norm_for_loop(X):
    cell,gene=X.shape
    dis=np.zeros((cell,cell))
    for i in range(cell):
        for j in range(i+1,cell):
            dis[i,j]=np.linalg.norm(X[i]-X[j],1)
    dis=dis+dis.T
    return dis

def sum_abs_for_loop(X):
    cell,gene=X.shape
    dis=np.zeros((cell,cell))
    for i in range(cell):
        for j in range(i+1,cell):
            dis[i,j]=np.sum(np.abs(X[i]-X[j]))
    dis=dis+dis.T
    return dis

def scipy_dist(X):
    dis=pdist(X,metric='cityblock')
    dis=squareform(dis)
    return dis

def numpy_dist(X):
    dis = np.abs(X[:, np.newaxis, :] - X[np.newaxis, :, :]).sum(axis=2)
    return dis

def record_file(file_name,time_sum):
    f = open(file_name, "w") 
    f.write("time is %f"%time_sum) 
    f.close()