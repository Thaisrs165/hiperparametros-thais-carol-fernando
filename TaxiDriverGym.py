import random
from IPython.display import clear_output
import gymnasium as gym
import numpy as np
from QLearning import QLearning
from numpy import loadtxt
env = gym.make("Taxi-v3").env
# only execute the following lines if you want to create a new q-table
alpha=0.1
gamma=0.9
epsilon=1.0
epsilon_min=0.01
epsilon_dec=0.995
episodes=100
qlearn = QLearning(env, alpha,gamma,epsilon,epsilon_min,epsilon_dec,episodes)

# Caso 1: Apenas exploração
q_learning_explore = QLearning(env, alpha, gamma, epsilon=1.0, epsilon_min=1.0, epsilon_dec=1.0, episodes=episodes)
q_learning_explore.train(q_learning_explore.select_action_explore, "data/explore_only.csv", "results/explore_only.png")

# Caso 2: Majoritariamente exploit
q_learning_exploit = QLearning(env, alpha, gamma, epsilon=0.1, epsilon_min=0.1, epsilon_dec=1.0, episodes=episodes)
q_learning_exploit.train(q_learning_exploit.select_action_exploit, "data/exploit_only.csv", "results/exploit_only.png")

# Caso 3: Decaimento de epsilon
q_learning_decay = QLearning(env, alpha, gamma, epsilon=1.0, epsilon_min=0.01, epsilon_dec=0.995, episodes=episodes)
q_learning_decay.train(q_learning_decay.select_action_decay, "data/epsilon_decay.csv", "results/epsilon_decay.png")






q_table = np.zeros([env.observation_space.n, env.action_space.n])

(state, _) = env.reset()
epochs, penalties, reward = 0, 0, 0
done = False
frames = [] # for animation
while (not done) and (epochs < 100):
    action = np.argmax(q_table[state])
    state, reward, done, t, info = env.step(action)

    if reward == -10:
        penalties += 1

    # Put each rendered frame into dict for animation
    frames.append({
        'frame': env.render(),
        'state': state,
        'action': action,
        'reward': reward
        }
    )
    epochs += 1
from IPython.display import clear_output
from time import sleep
clear_output(wait=True)
def print_frames(frames):
    for i, frame in enumerate(frames):
        clear_output(wait=True)
        print(frame['frame'])
        #print(frame['frame'].getvalue())
        print(f"Timestep: {i + 1}")
        print(f"State: {frame['state']}")
        print(f"Action: {frame['action']}")
        print(f"Reward: {frame['reward']}")
        sleep(.1)
print_frames(frames)
print("\n")
print("Timesteps taken: {}".format(epochs))
print("Penalties incurred: {}".format(penalties))


