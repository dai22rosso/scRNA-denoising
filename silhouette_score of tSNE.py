# -*- coding: utf-8 -*-
"""
Created on Wed May 22 17:01:43 2024

@author: rossoneri
"""
import numpy as np
import matplotlib.pyplot as plt
data=np.loadtxt("./score_tSNE.txt")
plt.figure(figsize=(15, 9))
plt.pcolormesh(data, cmap='viridis', shading='auto')
plt.colorbar(label='Color Gradient')
plt.title('silhouette_score')
plt.xlabel('learning_rate')
plt.ylabel('perplexity')
plt.show()