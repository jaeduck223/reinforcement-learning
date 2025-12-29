#step() 메서드 : 에이전트에게 행동을 시키는 메서드 -> 교재에 해당 코드가 없어서
#출판사에서 코드 다운 받아서 진행했음!
from gridworld import GridWorld

env = GridWorld()
action = 0
next_state, reward, done = env.step(action)

print('next_state :', next_state)
print('reward:', reward)
print('done:', done)
