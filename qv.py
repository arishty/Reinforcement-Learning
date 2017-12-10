import numpy as np


class QV:
    
    def __init__(self, world, alphaW=.1, alphaV=.1, beta=2):
        
        self.world = world
        self.w = np.zeros(world.n)              # vector of conditioned reinforcement values, one for each state
        #self.v = np.random.randint(5, size=(world.n, world.m))
        self.v = np.zeros((world.n, world.m))   # matrix of state-actions values
        self.alphaW = alphaW                    # learning rate for w
        self.alphaV = alphaV                    # learning rate for v
        self.beta = beta
        
    def probabilities(self, states):
        p = np.zeros((self.world.n, self.world.m))
        for s in range(states):
            initial = np.array((self.v[s, :] * self.beta))
            vexp = np.exp(initial) # vector of exponents
            vexp = vexp/sum(vexp)
            #print("p:")
            #print(p)
            #print("vexp:")
            #print(vexp)
            p[s] = vexp
            #print("final p:")
            #print (p)
            #p = np.concatenate(((p,vexp)), axis=0)
            #np.vstack((p,vexp))
            #p = np.append(p, vexp)
        return p
    
    def action(self, states, state):    #state is a vector of states
        pm = self.probabilities(states)
        pr = pm[state]
        print(self.v)
        choice = np.random.choice(self.v[state,:], p=pr)
        return self.v[state,:].tolist().index(choice)
    
    def learning(self,fromState, action, toState, world):
        totreward = world.values[toState] + self.w[toState]
        deltaV = self.alphaV * (totreward - self.v[fromState, action])
        self.v[fromState, action] += deltaV
        return self
    
    
    