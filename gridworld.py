"""
3*4 크기의 그리드 월드 생성
1. 에이전트는 상하좌우 4방향으로 이동 가능
2. 벽 안과 밖으로는 들어갈 수 없음.
3. 벽에 부딪히면 보상이 0이고
4. 사과는 +1, 폭탄은 -1, 그 외의 보상은 0이다.
5. 일회성 과제이며, 사과를 얻으면 게임은 종료됨.
"""
import numpy as np

class GridWorld:
    def __init__(self):
        self.action_space = [0, 1, 2, 3]  #행동 공간(가능한 행동)
        self.action_meaning = {           #행동의 의미
            0: 'up',
            1: 'down',
            2: 'left',
            3: 'right',
            }

        self.reward_map = np.array(
            [[0, 0, 0, 1.0],
             [0, None, 0, -1.0],
             [0, 0, 0, 0]]
            )
        self.goal_state = (0, 3)        #목표 상태
        self.wall_state = (1, 1)        #벽 상태
        self.start_state = (2, 0)       #시작 상태
        self.agent_state = self.start_state      #에이전트의 초기 상태

    def next_state(self, state, action):
        action_move_map = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        move = action_move_map[action]
        next_state = (state[0] + move[0], state[1] + move[1])
        ny, nx = next_state

        if nx < 0 or nx >= self.width or ny < 0 or ny >= self.height:
            next_state = state
        elif next_state == self.wall_state:
            next_state = state

        return next_state

    def reward(self, state, action, next_state):
        return self.reward_map[next_state]

    def render_v(self, v):
        for i in range(self.height):
            row = []
            for j in range(self.width):
                s = (i, j)
                if s == self.wall_state:
                    row.append(" W ")
                elif s == self.goal_state:
                    row.append(" G ")
                else:
                    val = V.get(s, 0.0)
                    row.append(f"{val:5.2f}")
            print("|".join(row))
        print()

    @property
    def height(self):
        return len(self.reward_map)

    @property
    def width(self):
        return len(self.reward_map[0])

    @property
    def shape(self):
        return self.reward_map.shape

    def actions(self):
        return self.action_space

    def states(self):
        for h in range(self.height):
            for w in range(self.width):
                yield(h, w) 

env = GridWorld()
V = {s : np.random.randn() for s in env.states()}
env.render_v(V)

print(env.height)
print(env.width)
print(env.shape)

for action in env.actions():
    print(action)

print('===')

for state in env.states():
    print(state)
