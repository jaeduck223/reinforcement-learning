#밴디트 머신을 이용해 실제 정책 동작을 구현 
import numpy as np
import matplotlib.pyplot as plt

class Bandit:
    def __init__(self, arms=10):        #arms=슬롯머신 대수
        self.rates = np.random.rand(arms) #슬롯머신 승률 설정(무작위)

    def play(self, arms):
        rate = self.rates[arms]
        if rate > np.random.rand():
            return 1
        else:
            return 0

#에이전트 구현 
class Agent:
    def __init__(self, epsilon, action_size=10):
        self.epsilon = epsilon          #무작위로 활동할 확률 
        self.Qs = np.zeros(action_size)
        self.ns = np.zeros(action_size)

    def update(self, action, reward):   #슬롯머신의 가치 추정
        self.ns[action] += 1
        self.Qs[action] += (reward - self.Qs[action]) / self.ns[action]

    def get_action(self):               #행동 선택(입실론 탐욕 정책)
        if np.random.rand() < self.epsilon:
            return np.random.randint(0, len(self.Qs)) #무작위 행동 선택
        return np.argmax(self.Qs)       #탐욕 행동 선택
#200번 수행한 뒤, 평균을 계산하여 출력하는 코드 
runs = 200
steps = 1000
epsilon = 0.1
all_rates = np.zeros((runs, steps))

for run in range(runs):
    bandit = Bandit()
    agent = Agent(epsilon)
    total_reward = 0
    rates = []

    for step in range(steps):
        action = agent.get_action()
        reward = bandit.play(action)
        agent.update(action, reward)
        total_reward += reward
        rates.append(total_reward / (step + 1))

    all_rates[run] = rates

avg_rates = np.average(all_rates, axis=0)

plt.ylabel('Rates')
plt.xlabel('Steps')
plt.title("200 average")
plt.plot(avg_rates)
plt.show()
