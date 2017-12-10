import playerQ2
import playerS2
import playerQV
import world
import sim

nRounds = 1000
rewardTotalQ = 0.0
rewardTotalS = 0.0
rewardTotalQV = 0.0

for i in range(nRounds):

    Npulls = 100 #number of times to pull bandit's arm
    
    sim = sim.Sim()
    world = world.World(stateNames=sim.stateNames, actionNames=sim.actionNames)
    
    world.P[:, world.states.index("small reward"), world.actions.index("leave")] = 1
    world.P[world.states.index("small taken"), world.states.index("small reward"), :] = 1
    world.P[world.states.index("large taken"), world.states.index("small reward"), :] = 1
    world.P[world.states.index("small reward"), world.states.index("large reward"), world.actions.index("wait")] = 1
    world.P[world.states.index("small reward"), world.states.index("small taken"), world.actions.index("take")] = 1
    world.P[world.states.index("large reward"), world.states.index("small reward"), world.actions.index("wait")] = 1
    world.P[world.states.index("large reward"), world.states.index("large taken"), world.actions.index("take")] = 1
    
    world.fixed=["small reward", "small taken", "large taken"]
    world.values=[-0.2, 1, -0.2, 5]
    
    pQ = playerQ2.PlayerQ(world)
    pS = playerS2.PlayerS(world)
    pQV = playerQV.PlayerQV(world)
    #print(str(i) + " " + str(pQ.rewardSoFar))
    
    for j in range (Npulls):
        #print(i)
        pQ.update()
        pS.update()
        pQV.update()
    
    rewardTotalQ += pQ.rewardSoFar
    rewardTotalS += pS.rewardSoFar
    rewardTotalQV += pQV.rewardSoFar
    
print ("Q learn average: " + str(rewardTotalQ  / nRounds))
print ("S learn average: " + str(rewardTotalS  / nRounds))
print ("QV learn average: " + str(rewardTotalQV  / nRounds))

#print ("Finished both!")
#print ("Q learn: " + str(pQ.rewardSoFar))
#print ("S learn: " + str(pS.rewardSoFar))


