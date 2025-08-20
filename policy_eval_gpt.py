from gridworld import GridWorld
from collections import defaultdict
import numpy as np

def eval_onestep(pi, V, env, gamma=0.9):
    # new_V를 defaultdict로 초기화 (기본값 0.0)
    new_V = defaultdict(float)
    
    for state in env.states():
        # 목표 상태는 가치 0으로 고정
        if state == env.goal_state:
            new_V[state] = 0.0
            continue

        v_state = 0.0
        # 정책에 따라 각 행동의 기댓값 누적
        for action, action_prob in pi[state].items():
            next_state = env.next_state(state, action)
            r = env.reward(state, action, next_state)
            v_state += action_prob * (r + gamma * V[next_state])
        
        new_V[state] = v_state

    return new_V


def policy_eval(pi, V, env, gamma, threshold=1e-3):
    while True:
        old_V = V.copy()
        V = eval_onestep(pi, V, env, gamma)

        # 상태별 최대 변화량(delta) 계산
        delta = max(abs(V[s] - old_V[s]) for s in env.states())

        if delta < threshold:
            break
    return V


if __name__ == "__main__":
    env = GridWorld()
    gamma = 0.9

    # 균등 정책 π 시작
    pi = defaultdict(lambda: {0: 0.25, 1: 0.25, 2: 0.25, 3: 0.25})
    # V도 defaultdict(float)로 초기화
    V = defaultdict(float)

    V = policy_eval(pi, V, env, gamma)
    env.render_v(V, pi)
