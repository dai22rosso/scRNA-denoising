import numpy as np
import os
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
file_position="./lower_dim_matrix"
# matrix= np.loadtxt()
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
def draw_3d(file,mat):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(mat[0, :], mat[1, :], mat[2, :], c='r', marker='o',s=0.005)
    plt.xlim(-50, 50)
    plt.ylim(-100,200)

    plt.savefig(file+"——order="+"012"+".png")
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(mat[0, :], mat[2, :], mat[1, :], c='r', marker='o',s=0.005)
    plt.savefig(file+"——order="+"021"+".png")
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(mat[2, :], mat[1, :], mat[0, :], c='r', marker='o',s=0.005)
    plt.savefig(file+"——order="+"210"+".png")
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(mat[2, :], mat[0, :], mat[1, :], c='r', marker='o',s=0.005)
    plt.savefig(file+"——order="+"201"+".png")
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(mat[1, :], mat[0, :], mat[2, :], c='r', marker='o',s=0.005)
    plt.savefig(file+"——order="+"102"+".png")
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(mat[1, :], mat[2, :], mat[0, :], c='r', marker='o',s=0.005)
    plt.savefig(file+"——order="+"120"+".png")
def draw_txt(file):
    mat=np.loadtxt(file)
    fname2=file[:-4]
    if(mat.shape[0]==0):
        plt.scatter([],[])
        plt.savefig((fname2+".png"))
        return
    if(len(mat)>100):
        mat=mat.T
    if(len(mat)==2):
        plt.figure()
        plt.scatter(mat[0],mat[1],s=0.005)
        plt.savefig((fname2+".png"))
        plt.show()
        return
    if(len(mat)==3):
        draw_3d(fname2, mat)
        return
X=get_filelist(file_position, [])
# for i in X:
#     if(i[-1]=="t"):
#         draw_txt(i)
print(X[37])
draw_txt(X[37])
    


