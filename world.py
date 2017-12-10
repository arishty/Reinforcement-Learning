import numpy as np

class World:
    
    def __init__(self, stateNames, actionNames):
        self.n = len(stateNames)
        self.m = len(actionNames)
        self.P = np.zeros((self.n,self.n,self.m))
        self.states = stateNames
        self.actions = actionNames
        self.values = np.zeros(self.n)
        self.start = self.states[0]
        self.fixed = []
        
    def nextState (self, fromState, action):
        self.P[fromState, 3, action]= 1
        p = self.P[fromState, :, action]
        return np.random.choice(self.states, p=p)
    
    
    
    
    
    
    
    
    
    
    
# world defines states and actions
# structured arrays
# one state 10 actions is bandit problem
# the 3 learning agents

####
#self.P = np.array((np.zeros(m*n^2)), dim=[n,n,m], dimnames=[stateNames, stateNames, actionNames])
#self.P = np.zeros(m*n^2, dtype={'names':['col1', 'col2'], 'formats':['i4','f4']})