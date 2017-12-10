import numpy as np

class BanditSimple:

    def __init__(self):
        
        self.arm_values = np.random.uniform(size=10)
        #(0,1,10)  # generate payout rates for the 10 machines, with a mean of 0, and standard deviation of 1 from the mean
        #self.K = np.zeros(10) # declare K, an array of size 10
        #self.est_values = np.zeros(10) # declare est_values, an array of size 10
        #print ("in init of bandit")

    def get_reward(self,action):    # generates noise, combines it with former arm_values array, returns combined array
        #noise = np.random.normal(0,1) # generates noise which averages to 0 in total and has a standard deviation of 1
        randomNum = np.random.uniform()
        if (randomNum <= self.arm_values[action]):
            reward = 1
        else:
            reward = 0
        return reward



# =============================================================================
#     def choose_eps_greedy(self,epsilon):
#         rand_num = np.random.random()
#         if epsilon>rand_num:
#           return np.random.randint(10)  # returns random integer < = 10
#         else:
#           return np.argmax(self.est_values) # return index of maximum value found in est_values array
# 
#     def update_est(self,action,reward):
#         self.K[action] += 1
#         alpha = 1./self.K[action]
#         self.est_values[action] += alpha * (reward - self.est_values[action]) # keeps running average of rewards
# 
# =============================================================================

