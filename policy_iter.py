from gridworld import GridWorld
from collections import defaultdict
from policy_eval_gpt import policy_eval

def argmax(d):
    max_value = max(d.values())
    max_key = 0
    for key, value in d.items():
        if value == max_value:
            max_key = key
    return max_key

def greedy_policy(V, env, gamma):   #탐욕 정책의 구현 
    pi = {}

    for state in env.states():
        action_values = {}

        for action in env.actions():
            next_state = env.next_state(state, action)
            r = env.reward(state, action, next_state)
            value = r + gamma * V[next_state]
            action_values[action] = value

        max_action = argmax(action_values)
        action_probs = {0: 0, 1: 0, 2: 0, 3: 0}
        action_probs[max_action] = 1.0
        pi[state] = action_probs
    return pi

action_values = {0: 0.1, 1: -0.3, 2: 9.9, 3: -1.3}
max_action = argmax(action_values)
print(max_action)

"""
env : 환경, gamma : 할인율, threshold : 정책 평가 시, 갱신을 중지하는 임게값
is_render : 정책 평가와 개선을 렌더링할 지에 대한 여부
"""
def policy_iter(env, gamma, threshold=0.001, is_render=False):  # 정책 반복법
    pi = defaultdict(lambda: {0:0.25, 1:0.25, 2:0.25, 3: 0.25})
    V = defaultdict(lambda: 0)

    while True:
        V = policy_eval(pi, V, env, gamma, threshold)    #평가 -> error 발생
        new_pi = greedy_policy(V, env, gamma)            #개선

        if is_render:
            env.render_v(V, pi)

        if new_pi == pi:
            break
        pi = new_pi

    return pi

env = GridWorld()
gamma = 0.9
pi = policy_iter(env, gamma)
