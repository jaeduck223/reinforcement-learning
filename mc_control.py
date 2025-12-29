from gridworld import GridWorld
from collections import defaultdict
from utils import greedy_probs
import numpy as np
import os, sys

#몬테카를로법으로 정책 제어를 구현함
def greedy_probs(Q, state, action_size=4):
    qs = [Q[(state, action)] for action in range(action_size)]
    max_action = np.argmax(qs)
    
    base_prob = epsilon / action_size
    action_probs = {action: 0.0 for action in range(action_size)}
    action_probs[max_action] += (1 - epsilon)
    return action_probs   #탐욕 행동을 취하는 행동을 반환

#입실론-탐욕 정책으로 정책 제어를 구현하는 함수를 선언
def greedy_probs_epsilon(Q, state, epsilon=0, action_size=4):
    qs = [Q[(state, action)] for action in range(action_size)]
    max_action = np.argmax(qs)

    base_prob = epsilon / action_size
    action_probs = {action: base_prob for action in range(action_size)}
    action_probs[max_action] += (1 - epsilon)
    return action_probs

class McAgent:
    def __init__(self):
       self.gamma = 0.9
       self.epsilon = 0.1
       self.alpha = 0.1
       self.action_size = 4

       random_actions = {0:0.25, 1:0.25, 2:0.25, 3:0.25}
       self.pi = defaultdict(lambda: random_actions)
       self.Q = defaultdict(lambda: 0)
       self.cnts = defaultdict(lambda: 0)   #self.cnts = defaultdict(lambda: 0)
       self.memory = []

    def get_action(self, state):
        action_probs = self.pi[state]
        actions = list(action_probs.keys())
        probs = list(actions_probs.values())
        return np.random.choice(actions, p=probs)

    def add(self, state, action, reward):
        data = (state, action, reward)
        self.memory.append(data)

    def reset(self):
        self.memory.clear() 

    def update(self):
        G = 0
        for data in reversed(self.memory):
            state, action, reward = data
            G = self.gamma * G + reward
            key = (state, action)
            # self.cnts[key] += 1
            # self.Q[key] += (G - self.Q[key]) / self.cnts[key] 
            self.Q[key] += (G - self.Q[key]) * self.alpha

            self.pi[state] = greedy_probs(self.Q, state, self.epsilon)  #state의 정책 탐욕화

#수정 전 
# self.Q[key] += (g - self.Q[key]) / self.cnts[state]
#수정 후(고정갑 alpha 방식으로 수행하는 개선 방법)
alpha = 0.1
self.Q[key] += (g - self.Q[key]) * alpha

env = GridWorld()
agent = McAgent()

episodes = 10000
for episode in range(episodes):
    state = env.reset()
    agent.reset()

    while True:
        action = agent.get_action(state)
        next_state, reward, done = env.step(action)

        agent.add(state, action, reward)
        if done:
            agent.update()
            break

        state = next_state

env.render_q(agent.Q) 
