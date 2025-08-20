from gridworld import GridWorld
from policy_iter import greedy_policy
from collections import defaultdict

#가치 반복법의 구현
def value_iter_onestep(V, env, gamma):
    for state in env.states():            #모든 상태에 차례대로 접근
        if state == env.goal_state:       #목표 상태에서의 가치 함수는 0이다.
            V[state] = 0
            continue

        action_values = []
        for action in env.actions():      #모든 행동에 차례대로 접근
            next_state = env.next_state(state, action)
            r = env.reward(state, action, next_state)
            value = r + gamma * V[next_state]   #새로운 가치 함수
            action_values.append(value)

        V[state] = max(action_values)           #최댓값을 추출
    return V

def value_iter(V, env, gamma, threshold=0.001, is_render=True):
    while True:
        if is_render:
            env.render_v(V)

        old_V = V.copy()                  #갱신 전 가치함수
        V = value_iter_onestep(V, env, gamma)
        #갱신된 양의 최댓값을 구함
        delta = 0
        for state in V.keys():
            t = abs(V[state] - old_V[state])
            if delta < t:
                delta = t
        #임계값과 비교 -> 가치 함수의 갱신량 최댓값이 임계값보다 작아질 때까지 계속 갱신
        if delta < threshold:
            break
    return V

V = defaultdict(lambda: 0)
env = GridWorld()
gamma = 0.9

V = value_iter(V, env, gamma)
pi = greedy_policy(V, env, gamma)
env.render_v(V, pi)
