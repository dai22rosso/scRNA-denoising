import numpy as np
import anndata as ad
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
def exist_inlist(elem,l):
    for i in range(len(l)):
        if (elem==l[i]):
            return True
    return False
def pca_svd(matrix, n_components):
    """
    使用SVD实现PCA降维。

    参数：
    matrix (numpy.ndarray): 需要降维的输入矩阵。
    n_components (int): 目标维度数。

    返回：
    numpy.ndarray: 降维后的矩阵。
    """
    # 确保输入矩阵是numpy数组
    matrix = np.array(matrix)
    
    # 中心化数据
    matrix_mean = np.mean(matrix, axis=0)
    centered_matrix = matrix - matrix_mean
    
    # 使用SVD分解矩阵
    U, S, Vt = np.linalg.svd(centered_matrix, full_matrices=False)
    
    # 选择前n_components个奇异值和对应的向量
    U_reduced = U[:, :n_components]
    S_reduced = S[:n_components]
    Vt_reduced = Vt[:n_components, :]
    
    # 计算降维后的矩阵
    reduced_matrix = np.dot(U_reduced, np.diag(S_reduced))
    
    return reduced_matrix
# def pca(X,k):
#     U_new=U[:,:(k-1)]
#     data=(np.transpose(U_new)@X.T)
#     return data
# adata=ad.read_h5ad('./pancreas.h5ad')
# a=adata[6321:8258]

# print(a.obs['celltype'])
# X=pd.DataFrame(a.obs['celltype'])
# print(X.to_numpy())
# l=X.to_numpy()
label=np.loadtxt('./label.txt',dtype=str).tolist()
# np.savetxt('./label.txt', X.to_numpy(),fmt='%s')
elem=['acinar', 'beta', 'delta', 'activated_stellate', 'ductal', 'alpha', 'epsilon', 'gamma', 'endothelial', 'quiescent_stellate', 'macrophage', 'schwann', 'mast', 't_cell']
mat=np.loadtxt("./inDrop1.txt")
label_colors = {
    'acinar': 'red', 'beta': 'blue', 'delta': 'green', 'activated_stellate': 'purple',
    'ductal': 'orange', 'alpha': 'brown', 'epsilon': 'pink', 'gamma': 'gray',
    'endothelial': 'olive', 'quiescent_stellate': 'cyan', 'macrophage': 'magenta',
    'schwann': 'yellow', 'mast': 'lime', 't_cell': 'teal'
}
colors=[]
for i in range(1937):
    mm=label_colors[(label[i])]
    colors.append(mm)
print(colors)
# a=to_numpy(a)
mat=pca_svd(mat,50)
print("PCA:",mat.shape)
tsne = TSNE(n_components=2,perplexity=40, learning_rate=5,method="barnes_hut")
data= tsne.fit_transform(mat)
print(data.shape)
plt.figure(figsize=(10,10))
idx=[]
for j in range(14):
    idx.append(label.index(elem[j]))
for i in range(1937):
    if(exist_inlist(i, idx)):
        ll=label[i]
        plt.scatter(data[i,0], data[i,1], c=colors[i],s=10,label=ll)
    else:

        plt.scatter(data[i,0], data[i,1], c=colors[i],s=10)

plt.title('tSNE Dim=2 graph')
plt.xlabel('tSNE Dimension 1')
plt.ylabel('tSNE Dimension 2')
plt.legend(markerscale=2)
plt.show()
# # mat=np.array([[1,2,3,4],[5,6,7,8],[1,2,3,4]])
# fname="./lower_dimension_data/dim_tSNE="
# per=[20,50,75,100,200,500,750,1000,2000,3500,5000,7500,10000]
# lr=[10,20,50,100,200,500,1000,2000,5000]

# for i in range(13):
#     for k in range(9):
#         perx=per[i]
#         lrate=lr[k]
#         tsne = TSNE(n_components=2,perplexity=perx, learning_rate=lrate,method="barnes_hut")
#         data= tsne.fit_transform(X)
#         fname1=fname+"perplexity="+str(perx)+"learning_rate="+str(lrate)+"barnes_hut_"+"2.txt"
#         np.savetxt(fname1, data)

# for i in range(len(mat)):
#     if(i % 150==0):
#         print(i/150)
#     for j in range(len(mat[0])):
#         num=int(mat[i][j]*10)
#         if(num==0):
#             continue
#         if(num<100):
#             distribution[int(num)]+=1
#         else:
#             distribution[-1]+=1
# for i in range(len(mat)):
#     if(i % 150==0):
#         print(i/150)
    
#     num=int(mat[i]*10)
#     if(num==0):
#         continue
#     if(num<100):
#         distribution[int(num)]+=1
#     else:
#         distribution[-1]+=1
            

