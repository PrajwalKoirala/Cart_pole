import numpy as np     # imports numpy
import gym             # imports gym

env = gym.make('CartPole-v1')       # creates CartPole environment
new_state = env.reset()             # env.reset() resets the cartpole and returns the new state
done =   False                      # whether the simulation of one episode has completed on not
actions = [0, 1]                    # list of possible actions : 0 corresponds to "pushing the cart to the left" and 1 correspinds to "pushing the cart to the left"


while not done:
    action = np.random.choice(actions)                    # make a random choice from actions = [0, 1]
    new_state, reward, done, info = env.step(action)      # make a step taking the 'action', in return we get updated state, corresponding reward, boolean representing whether the simulation has completed, and info that we can ignore
    env.render()                                          # to render the environment 
env.close()                                               # closes the viewer
