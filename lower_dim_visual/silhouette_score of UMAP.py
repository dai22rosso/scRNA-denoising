# -*- coding: utf-8 -*-

from sklearn.metrics import silhouette_score
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
import numpy as np
import os
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
def get_filelist(dir, Filelist):
 
    newDir = dir
 
    if os.path.isfile(dir):
 
        Filelist.append(dir)
 
        # # 若只是要返回文件文，使用这个
 
        # Filelist.append(os.path.basename(dir))
 
    elif os.path.isdir(dir):
 
        for s in os.listdir(dir):
 
            # 如果需要忽略某些文件夹，使用以下代码
 
            #if s == "xxx":
 
                #continue
 
            newDir=os.path.join(dir,s)
 
            get_filelist(newDir, Filelist)
 
    return Filelist
def get_per_lr(file):
    lr=0
    per=0
    num=[1,2,3,4,5,6,7,8,9,0]
    pert=[5,10,15,20,35,50,75,100,150,200,250,300,350,500,750,1000]
    lrt=[5,10,15,20,30,40,50,75,100]
    for i in range(len(file)):
        if(file[i]=='t'):
            if(i<(len(file)-1)):
                if(file[i+1]=='e'):
                    lr=i+2
                if(file[i+1]=='y'):
                    per=i+2
    lr_end=lr
    per_end=per
    while(file[lr_end]!='b'):
        lr_end+=1
    while(file[per_end]!='l'):
        per_end+=1
    p=file[(per+1):per_end]
    l=file[(1+lr):lr_end]
    return pert.index(int(p)),lrt.index(int(l))
                
                    
    
    
    
    
def get_score(file,x,y,z):
    l=[]
    for i in range(len(x)):
        if(y[i]>z[i]):
            l.append(-1)
            continue
        yb=y[i]
        zb=z[i]
        xb=x[i]
        if(y[i]>=1):
            yb=int(y[i])
        if(z[i]>=1):
            zb=int(z[i])
        if(x[i]>=1):
            xb=int(x[i])
        
        fname=file+"/UMAP_withoutstandard=dist="+str(yb)+"nbor_amount="+str(xb)+"spread="+str(zb)+"dim=3.txt"
        mat=np.loadtxt(fname)
        kmeans = KMeans(n_clusters=14, random_state=42,n_init='auto')
        labels = kmeans.fit_predict(mat)
        sil_score = silhouette_score(mat, labels)
        l.append(sil_score)
        if(i%100==0):
            print(i/100)
    return l
    
def get_index(x,l):
    j=[]
    for i in x:
       j.append(l.index(i))
    return j 
        
file_position="./Umap_without_standard"
per=[5,10,15,20,35,50,75,100,150,200,250,300,350,500]
dis=[0.1,0.2,0.5,1,2,5,10,20,50,100,150,200]
spread=[0.5,1,2,5,10,20,50,100,200,500,1000,2000]
x, y, z = np.meshgrid(per, dis, spread)
x = x.flatten()
y = y.flatten()
z = z.flatten()
print(len(x),len(y),len(z))
fig = plt.figure(figsize=(80, 80))
ax = fig.add_subplot(111, projection='3d')
values=get_score(file_position, x, y, z)
print(len(values))
# 使用 scatter 绘制三维颜色渐变图
x=get_index(x,per)
y=get_index(y,dis)
z=get_index(z,spread)
sc = ax.scatter(x,y,z, c=values, cmap='viridis',s=2000)

# 添加颜色条
fig.colorbar(sc, ax=ax, shrink=0.5, aspect=5, label='Color Gradient')

# 设置标题和标签
ax.set_title('3D Scatter Plot with Color Gradient')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')

plt.show()