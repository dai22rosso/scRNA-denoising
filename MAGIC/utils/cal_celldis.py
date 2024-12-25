import numpy as np
def manhatten(list1,list2):
    s=0
    for i in range(len(list1)):
        s+=abs(list1[i]-list2[i])
    return s
def euclid(list1,list2):
    s=0
    for i in range(len(list1)):
        s+=(list1[i]-list2[i])**2
    return s**0.5
X=np.loadtxt('./inDrop1.txt')
X1=np.loadtxt('./inDrop1_cp10k.txt')
X2=np.loadtxt('./inDrop1_logcp10k.txt')
X3=np.loadtxt('./inDrop1_sqrtcp10k.txt')
X=np.array(X,dtype=int)
X1=np.array(X1,dtype=int)
X2=np.array(X2,dtype=int)
X3=np.array(X3,dtype=int)
dis=np.zeros([len(X),len(X)])
dis1=np.zeros([len(X),len(X)])
dis2=np.zeros([len(X),len(X)])
dis3=np.zeros([len(X),len(X)])
for i in range(len(X)):
    if(i%100==0):
        print(i/100)
    for j in range(len(X)):
        if(i>j):
            d=manhatten(X[i],X[j])
            dis[i][j]=d
            d1=manhatten(X1[i],X1[j])
            dis1[i][j]=d1
            d2=manhatten(X2[i],X2[j])
            dis2[i][j]=d2
            d3=manhatten(X3[i],X3[j])
            dis3[i][j]=d3            
np.savetxt('celldis_no_norm.txt',dis)
np.savetxt('celldis_cp10k.txt',dis1)
np.savetxt('celldis_log_cp10k.txt',dis2)
np.savetxt('celldis_sqrt_cp10k.txt',dis3)
