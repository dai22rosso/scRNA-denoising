import numpy as np
import time
from utils import *
import scipy as sp
from scipy.spatial.distance import pdist
from scipy.spatial.distance import squareform
X=np.loadtxt('inDrop1.txt')
X=np.array(X,dtype=int)
time_stamp1=time.time()
dis1=norm_for_loop(X)
time_stamp2=time.time()
run_time=time_stamp2-time_stamp1
record_file('norm_for_loop_runtime.txt',run_time)
np.savetxt('norm_for_loop.txt',dis1,fmt='%d')
time_stamp2=time.time()
dis2=sum_abs_for_loop(X)
time_stamp3=time.time()
run_time=time_stamp3-time_stamp2
record_file('sum_abs_for_loop_runtime.txt',run_time)
np.savetxt('sum_abs_for_loop.txt',dis2,fmt='%d')
time_stamp3=time.time()
dis3=scipy_dist(X)
time_stamp4=time.time()
run_time=time_stamp4-time_stamp3
record_file('scipy_dist_runtime.txt',run_time)
np.savetxt('scipy_dist.txt',dis3,fmt='%d')
time_stamp4=time.time()
dis4=numpy_dist(X)
time_stamp5=time.time()
run_time=time_stamp5-time_stamp4
record_file('numpy_dist_runtime.txt',run_time)
np.savetxt('numpy_dist.txt',dis4,fmt='%d')

