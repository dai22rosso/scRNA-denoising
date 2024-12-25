import numpy as np
import matplotlib.pyplot as plt

X=np.loadtxt('inDrop1.txt')
dis = np.abs(X[:, np.newaxis, :] - X[np.newaxis, :, :]).sum(axis=2)