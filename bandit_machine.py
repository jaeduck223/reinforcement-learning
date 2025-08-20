#밴디트 머신 구현
import numpy as np

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

#슬롯머신 작동 부분 
bandit = Bandit()
for i in range(7):
    print(bandit.play(7))
