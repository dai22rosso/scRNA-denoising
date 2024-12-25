import numpy as np

def classify(l):
    """
    hard to describe, let me show an example: transfer [0,2,3,3,4] to [1,0,1,2,1]
    """
    p=np.ones(np.max(l)+1)-1
    for i in range(len(l)):
        p[l[i]]+=1
    return p
def calculate_nb_parameters(mu_zinb, sigma2_zinb, beta):
    """
    given the fixed zero inflation rate,
    calculate the NB distribution parameter in this ZINB distribution
    
    """
    mu_nb = mu_zinb / (1 - beta)

    sigma2_nb = (sigma2_zinb - beta * (1 - beta) * mu_zinb ** 2) / (1 - beta)
    r = mu_nb ** 2 / (sigma2_nb - mu_nb)
    p = r / (r + mu_nb)
    return r,p
def get_zeroinflated(l):
    """
    given the list, get the zero inflation
    precision is about 0.01 and we use the height of 1/height of 2 to measure the ZINB fit precision
    """
    l=np.array(l)
    mu=np.mean(l)
    sig=np.var(l)
    ratio=[]
    for i in range(100):
        r,p=calculate_nb_parameters(mu,sig,0.01*i) #get the NB parameter
        if(r<=0 or p>=1):
            ratio.append(1e9)
            continue # if the NB doesn't exist, then this ZINB can't stand
        a=classify(l) # get how much 1 and 2 we have in ZINB
        if(np.sum(a)==0):
            ratio.append(1e9)
            continue
        a1=a[1]/np.sum(a)
        a2=a[2]/np.sum(a)
        ra=(a1+(1e-9))/(a2+(1e-11))
        rb=2/(r+1)/(1-p)
        ratio.append(ra/rb)
        #prevent the division error

            #compare the value with 1
    for i in range(len(ratio)):
        ratio[i]=abs(ratio[i]-1)
    idx=ratio.index(np.min(ratio))
    return idx/100


# X=np.loadtxt('./inDrop1.txt')
# X=np.array(X,dtype=int)
# zero_infla=[]
# for m in range(5000):
#     if(m % 1000 ==0):
#         print(m/1000)
#     l=X[:,m]
#     a=classify(l)
#     if(len(a)<=2):
#         zero_infla.append(-1)
#     else:
#         zero_infla.append(get_zeroinflated(l))
# np.savetxt('zero_infla_rate.txt',zero_infla)