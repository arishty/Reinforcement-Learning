import sarsa2
import bandit2
# split into 2 classes, Q and S players
# understand and fix sarsa class code
class PlayerS:

    def __init__(self, world):
        
        self.ai = sarsa2.Sarsa(world)
        self.lastState = None
        self.lastAction = None
        self.nextAction = None
        self.arms = bandit2.BanditSimple()
        self.rewardSoFar = 0
        

    def update(self):
        
        # why are we saving lastAction? what are we doing with it?
        # can we use that instead of nextAction? do we need both?
        # should we create playerQ and playerS classes instead of this 
        #mess?
        
        state = 0
  
        if (self.nextAction == None):  #first time that update is called, there is no precomputed next Action
            action = self.ai.chooseAction(state)
        else:
            action = self.nextAction
            
        
        self.lastState = 0
        self.lastAction = action
        
        #state = 1
        reward = self.arms.get_reward(action)
        self.rewardSoFar += reward
        #print("state " + str(state) + " action: " + str(action) + "reward: " + str(reward) + " reward so far: " + str(self.rewardSoFar))
    
        self.nextAction = self.ai.chooseAction(state)
        self.ai.learn(self.lastState, self.lastAction, reward, state, self.nextAction)

            






