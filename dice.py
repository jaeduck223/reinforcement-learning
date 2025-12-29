#주사위 2개를 던지는 문제를 통해 샘플 모델을 구현
import numpy as np

#주사위를 2개 던져서 합을 구하는 함수
def sample(dices=2):
    x = 0
    for _ in range(dices):
        x += np.random.choice([1, 2, 3, 4, 5, 6])  #주사위를 굴림
    return x

print(sample())
print(sample())
print(sample())

trial = 10000                       #샘플링 횟수 -> 늘릴수록 정답에 가까워짐(몬테카를로 원리)

samples = []
for _ in range(trial):             #샘플링
    s = sample()
    samples.append(s)

V = sum(samples) / len(samples)    #평균 계산
print(V)

#증분 방식을 이용한 평균 구하기
trial = 1000
V, n = 0, 0

for _ in range(trial):
    S = sample()
    n += 1
    V += (s - V) / n   #증분 방식의 수식 
print(V)
