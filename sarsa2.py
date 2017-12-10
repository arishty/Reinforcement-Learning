import random

class Sarsa:
    def __init__(self, world, epsilon=0.1, alpha=0.2, gamma=0.9):     # definition of class and attributes
        self.q = {}
        self.world = world
        self.epsilon = epsilon
        self.alpha = alpha
        self.gamma = gamma

    def getQ(self, state, action):
        return self.q.get((state, action), 0.0)
        # return self.q.get((state, action), 1.0)
        
    def learnQ(self, state, action, reward, value):
        oldv = self.q.get((state, action), None)    # old value
        if oldv is None:
            self.q[(state, action)] = reward
        else:
            self.q[(state, action)] = oldv + self.alpha * (value - oldv)    

    def chooseAction(self, state):                  # implementation of exploration/exploitation balance
                                                    # Exploration:
        if random.random() < self.epsilon:          # if the randomly generated value is less than epsilon...
            action = random.choice(self.world.actions)    # ...a random action is chosen from actions array and assigned to variable "action"
                                                    # Exploitation:
        else:                                       # if the randomly generated value is NOT less than epsilon...
            q = [self.getQ(state, a) for a in self.world.actions]     # create array "q" of Q values for state/action pairs encountered
            maxQ = max(q)                                       # define "max" variable as maximum value found in array q
            count = q.count(maxQ)                               # counts to see if there are multiple maximum values (which are equal)
            if count > 1:                                       # if there is more than one maximum value
                best = [i for i in range(len(self.world.actions)) if q[i] == maxQ]
                i = random.choice(best)                         # randomly choose one of them and assign it to variable "i"
            else:                                               # if there's one maximum value
                i = q.index(maxQ)                               # assign its array index to variable "i"

            action = self.world.actions[i]                            # choose the action from the array self.actions with index i and assign it to variable "action"
        return action 

        
    def learn(self, state1, action1, reward, state2, action2):
        qnext = self.getQ(state2, action2)
        self.learnQ(state1, action1,
                    reward, reward + self.gamma * qnext)

