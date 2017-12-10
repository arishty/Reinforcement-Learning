import qlearn2
import bandit2
# split into 2 classes, Q and S players
# understand and fix sarsa class code
class PlayerQ:

    def __init__(self, world):
      
        self.ai = qlearn2.QLearn(world)
        self.lastState = None
        self.lastAction = None
        #self.nextAction = None
        #self.arms = bandit2.BanditSimple()
        self.rewardSoFar = 0

 
    def update(self):
        
        state = 0
        
        action = self.ai.chooseAction(state)
        self.lastState = 0
        self.lastAction = action
        
        state = 0
        
        action = self.ai.chooseAction(state)
        #reward = self.arms.get_reward(action)
        #self.rewardSoFar += reward
        #print("state " + str(state) + " action: " + str(action) + "reward: " + str(reward) + " reward so far: " + str(self.rewardSoFar))
        self.ai.learn(self.lastState, self.lastAction, reward, state)
       
