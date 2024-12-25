# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 03:46:57 2024

@author: rossoneri
"""

import numpy as np


def cp10k(array: np.ndarray) -> np.ndarray:
    """Normalize data to counts per 10,000."""
    size_factors = array.sum(axis=1) / 1e4
    normalized_array = array / size_factors[:, None]
    return normalized_array

def log_cp10k(array: np.ndarray) -> np.ndarray:
    """Normalize data to log counts per 10,000."""
    normalized_array = cp10k(array)
    log_normalized_array = np.log1p(normalized_array)
    return log_normalized_array

def sqrt_cp10k(array: np.ndarray) -> np.ndarray:
    """Normalize data to sqrt counts per 10,000."""
    normalized_array = cp10k(array)
    sqrt_normalized_array = np.sqrt(normalized_array)
    return sqrt_normalized_array
# 示例 numpy 数组
array = np.loadtxt('inDrop1.txt')

# 执行 cp10k 归一化
cp10k_normalized = cp10k(array)
np.savetxt('inDrop1_cp10k.txt', cp10k_normalized)

# 执行 log_cp10k 归一化
log_cp10k_normalized = log_cp10k(array)
np.savetxt('inDrop1_logcp10k.txt', log_cp10k_normalized)

# 执行 sqrt_cp10k 归一化
sqrt_cp10k_normalized = sqrt_cp10k(array)
np.savetxt('inDrop1_sqrtcp10k.txt', sqrt_cp10k_normalized)