import random

def estimate_pi(n):
    points_inside_circle = 0
    points_inside_square = 0

    for _ in range(n):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        distance = x**2 + y**2

        if distance <= 1:
            points_inside_circle += 1
        points_inside_square += 1

    pi = 4 * (points_inside_circle / points_inside_square)
    return pi

# 시뮬레이션 횟수 설정
num_simulations = 100

# 원주율 추정
estimated_pi = estimate_pi(num_simulations)

print("Estimated Pi:", estimated_pi)
