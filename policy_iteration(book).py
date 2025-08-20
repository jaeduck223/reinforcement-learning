#반복적 정책 평가 알고리즘 구현
from gridworld import GridWorld
from collections import defaultdict
"""
pi : 정책, V : 가치 함수, env : 환경, gamma : 할인율

"""
def eval_onestep(pi, V, env, gamma=0.9): #가치 함수의 업데이트 기능 구현 함수
    for state in env.states():           #각 상태에 접근
        if state == env.goal_state:      #목표 상태에서는 가치 함수는 항상 '0'
            V[state] = 0
            continue
        action_probs = pi[state]         #probs : 확률
        new_V = 0
        #각 행동에 접근하는 부분
        for action, action_prob in action_probs.items():
            next_state = env.next_state(state, action)
            r = env.reward(state, action, next_state)
            new_V += action_prob * (r + gamma * V[next_state])  #새로운 가치 함수

        V[state] = new_V

    return V

def policy_eval(pi, V, env, gamma, threshold=0.001):
    while True:
        old_V = V.copy()    #갱신 전 가치 함수
        V = eval_onestep(pi, V, env, gamma)

        delta = 0           #갱신된 양의 최댓값 계산
        for state in V.keys():
            t = abs(V[state] - old_V[state])
            if delta < t:
                delta = t

        if delta < threshold: #임계값 계산
            break
    return V

env = GridWorld()
gamma = 0.9
pi = defaultdict(lambda: {0: 0.25, 1:0.25, 2:0.25, 3:0.25})
V = defaultdict(lambda: 0)

V = policy_eval(pi, V, env, gamma)
env.render_v(V, pi)   #error 생기는 부분 
