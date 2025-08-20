#표본 평균을 구하는 코드
import numpy as np

np.random.seed(0)
rewards = []

for n in range(1, 11):
    reward = np.random.rand()
    rewards.append(reward)
    Q = sum(rewards) / n
    print(Q)

#0번째 슬롯머신의 가치를 계산 
Q = 0
for n in range(1, 11):
    reward = np.random.rand()
    Q = Q + (reward - Q) / n
    print(Q)
# Q = Q + (reward - Q) / n
Q += (reward - Q) / n
print('Q :', Q)

#0번째 슬롯머신을 10번 연속으로 플레이하고
#보상을 받을 때마다 슬롯머신의 가치 추정치를 계산함.
