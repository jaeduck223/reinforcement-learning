#defaultdict 라이브러리 사용법 코드(2)
from collections import defaultdict
from gridworld import GridWorld

env = GridWorld()
V = defaultdict(lambda: 0)
state = (1, 2)
print(V[state])

pi = defaultdict(lambda: {0: 0.25, 1: 0.25, 2: 0.25, 3: 0.25})
state = (0, 1)
print(pi[state])
