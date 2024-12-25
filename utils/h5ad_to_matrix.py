import numpy as np
import anndata as ad
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE

def normalize_counts_per_10k(matrix, target_sum=1e4):
    """
    将输入的计数矩阵标准化为每1万个计数。
    
    参数：
        matrix (numpy.ndarray): 输入的计数矩阵（细胞 x 基因）。
        target_sum (float): 目标总计数值。
        
    返回：
        numpy.ndarray: 处理后的矩阵。
    """
    # 计算每个细胞的总计数
    total_counts_per_cell = matrix.sum(axis=1)
    
    # 计算归一化因子
    scaling_factors = target_sum / total_counts_per_cell
    
    # 应用归一化因子，将每个基因的计数乘以归一化因子
    normalized_matrix = matrix * scaling_factors[:, np.newaxis]
    
    return normalized_matrix
def normalize_and_log_transform(matrix, target_sum=1e4):
    """
    将输入的计数矩阵标准化为每1万个计数，并进行对数转换。
    
    参数：
        matrix (numpy.ndarray): 输入的计数矩阵（细胞 x 基因）。
        target_sum (float): 目标总计数值。
        
    返回：
        numpy.ndarray: 标准化并对数转换后的矩阵。
    """
    # 计算每个细胞的总计数
    total_counts_per_cell = matrix.sum(axis=1)
    
    # 计算归一化因子
    scaling_factors = target_sum / total_counts_per_cell
    
    # 应用归一化因子，将每个基因的计数乘以归一化因子
    normalized_matrix = matrix * scaling_factors[:, np.newaxis]
    
    # 对数转换，使用自然对数
    log_transformed_matrix = np.log1p(normalized_matrix)
    
    return log_transformed_matrix

X=np.loadtxt('inDrop1.txt')
normalized_matrix=normalize_counts_per_10k(X)
normalized_log_matrix = normalize_and_log_transform(X)
np.savetxt('./inDrop1_cp10k&log.txt', normalized_log_matrix)
np.savetxt('./inDrop1_cp10k.txt', normalized_matrix)
print(normalized_log_matrix)
