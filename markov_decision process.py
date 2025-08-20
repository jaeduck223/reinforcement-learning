#마르코프 결정 과정 -> 등비수열의 합 구하기  

v = 1
for i in range(1, 100):
    v += -1 * (0.9 ** i)
print(v)
