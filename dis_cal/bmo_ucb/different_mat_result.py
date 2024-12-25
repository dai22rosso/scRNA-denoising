from dis_utils import *
import time

def generate_sparse_matrix(width, height, sparsity, max_value=100):

    matrix = np.zeros((height, width), dtype=int)


    num_nonzeros = int((1 - sparsity) * width * height)


    indices = np.random.choice(width * height, num_nonzeros, replace=False)


    matrix.flat[indices] = np.random.randint(1, max_value + 1, size=num_nonzeros)

    return matrix


width=[100,1000,10000,100000,500000,1000000,2000000,3000000]
spar=[0,0.2,0.5,0.9]
# timen=np.zeros([3,8,4])
for i in range(8):
    print(i)
    for j in range(4):
        mat=generate_sparse_matrix(width[i],width[i],spar[j],20)
        np.savetxt('mat'+'dim'+str(i)+'spar'+str(j)+'.txt',mat)
        # time_start = time.time()
        # norm_for_loop(mat)
        # time_end = time.time() 
        # time_sum = time_end - time_start
        # timen[0][i][j]=time_sum
        # time_start = time.time()
        # sum_abs_for_loop(mat)
        # time_end = time.time() 
        # time_sum = time_end - time_start
        # timen[1][i][j]=time_sum
        # time_start = time.time()
        # scipy_dist(mat)
        # time_end = time.time() 
        # time_sum = time_end - time_start
        # timen[2][i][j]=time_sum

