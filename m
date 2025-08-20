#가치 함수의 딕셔너리 구현
from gridworld import GridWorld

env = GridWorld()
V = {}

for state in env.states():
    V[state] = 0

state = (1, 2)
print(V[state])
