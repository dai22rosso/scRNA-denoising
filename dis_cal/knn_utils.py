import numpy as np
import scipy as sp
from sklearn.neighbors import NearestNeighbors
import time
from scipy.spatial import KDTree
from sklearn.neighbors import BallTree
from dis_utils import *
def numpy_argsort(D,k):
    time_stamp1=time.time()
    indices = np.argsort(D,axis=1)[:,:k]
    time_stamp2=time.time()
    run_time=time_stamp2-time_stamp1
    file_name='numpy_argsort_runtime_of_k=%d.txt'%k
    # record_file(file_name,run_time)
    return indices
def sklearn_knn(D,k):
    time_stamp1=time.time()
    nbrs = NearestNeighbors(n_neighbors=k, algorithm='auto').fit(D)
    A=nbrs.kneighbors(D, return_distance=False)
    time_stamp2=time.time()
    run_time=time_stamp2-time_stamp1
    file_name='sklearn_knn_runtime_of_k=%d.txt'%k
    record_file(file_name,run_time)
    return A
def kdtree_knn(D,k):
    tree = KDTree(D)
    time_stamp1=time.time()
    dis,A=tree.query(D,k)
    time_stamp2=time.time()
    run_time=time_stamp2-time_stamp1
    file_name='kdtree_knn_runtime_of_k=%d.txt'%k
    record_file(file_name,run_time)
    return A
def balltree_knn(D,k):
    tree = BallTree(D)
    time_stamp1=time.time()
    dis,A=tree.query(D,k)
    time_stamp2=time.time()
    run_time=time_stamp2-time_stamp1
    file_name='balltree_knn_runtime_of_k=%d.txt'%k
    record_file(file_name,run_time)
    return A
