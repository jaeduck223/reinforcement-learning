#defaultdict 라이브러리 사용법 코드(1)
from gridworld import GridWorld

env = GridWorld()
V = {}

for state in env.states():
    V[state] = 0

state = (1, 2)
print(V[state])
