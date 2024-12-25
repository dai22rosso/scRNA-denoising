import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

# l=np.zeros(11)
X=np.loadtxt('./inDrop1_cp10k&log.txt')

# for m in range(len(X)):
    
#     for j in range(len(X[0])):
#         i=X[m][j]
#         # if(i<0.1):
#         #     continue
#         if(int(i)<10):
#             if(int(i)==0):
#                 print('yes')
#             l[int(i)]+=1
#         else:
#             l[-1]+=1
# print(l)
# plt.plot(l)
plt.figure(figsize=(5.12,1.28))
Y=np.clip(X, 0,2000)
cmap = plt.get_cmap('viridis')  # 选择一个颜色映射
norm = mcolors.Normalize(vmin=0, vmax=4)  # 定义归一化范围

# 绘制渐变色图
plt.imshow(Y, cmap=cmap, norm=norm)
plt.colorbar(label='Value')
plt.title('Gradient Color Map')
plt.savefig('./inDrop1distribution_cp10k&log.png', dpi=100)