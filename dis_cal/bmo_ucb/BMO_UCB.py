import numpy as np
import scipy as sp
# from bmo_utils import *

b_arm_amount=10
a_arm_amount=10
pull_dim_once=10
class UCB:
    def __init__(self,arm_array,delta,n_best_arms=10,n_extra_arms=10,sample_size=100):
        self.arms_container = arm_array
        self.number_of_arms = len(arm_array)
        self.log_delta_inverse = max(np.log(1/delta), 0.0)
        self.global_sigma = float('nan')
        self.global_number_of_pulls = 0
        self.global_sum_of_pulls = 0
        self.global_sum_of_squares_of_pulls = 0
        self.number_of_best_arms = n_best_arms
        self.number_of_extra_arms = n_extra_arms
        self.sample_size = sample_size
        self.arm_states = [{'pulls' : 0,
        'sum' : 0.0,
        'sum_of_squares' : 0.0,
        'ucb' : np.inf,
        'lcb' : -np.inf,
        'est_mean' : 0.0} for i in range(self.number_of_arms)]
        self.arms_to_keep = set()
        self.arms = arm_array
        self.final_number_of_pulls = {}
        self.final_sorted_order = []
        self.arms_brute = []
        self.top_k_arms = []

    def pull_arm(self,arm):
        if(self.arm_states[arm]['pulls']==(dim-1)/pull_dim_once):
            temp=np.average(self.arms[arm])
            self.arm_states[arm]['est_mean']=temp
            self.arm_states[arm]['ucb']=temp
            self.arm_states[arm]['lcb']=temp
            self.arm_states[arm]['pulls']+=1
            self.arm_states[arm]['sum']=temp*dim 
            self.arm_states[arm]['sum_of_squares']=np.sum(self.arms[arm]**2)
        else:
            temp_pull=np.random.randint(0,dim-1,pull_dim_once)
            temp_pull=self.arms[arm][temp_pull]
            self.arm_states[arm]['pulls']+=1
            self.arm_states[arm]['sum']+=np.sum(temp_pull)
            self.arm_states[arm]['sum_of_squares']+=np.sum(temp_pull**2)
            sigma=self.arm_states[arm]['sum_of_squares']/10/self.arm_states[arm]['pulls']-(self.arm_states[arm]['sum']/10/self.arm_states[arm]['pulls'])**2
    def update_var(self,arm):
        self.global_sigma=self.global_sum_of_squares_of_pulls/self.global_number_of_pulls-(self.global_sum_of_pulls/self.global_number_of_pulls)**2
    
    def initialize(self,initial_pulls):
        return
    
X  = np.random.randint(0, 100, 100000)
arm_assemb= UCB(X,0.1,2,0,100)
arm_assemb.initialize(1)



    
            