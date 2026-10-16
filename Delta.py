from math import sqrt


def delta(a, b, c):

    delta: float = b * b - 4 * a * c
    print(f"判别式 Delta = {delta}")

    if delta > 0:
        x1: float = (-b + sqrt(delta)) / (2 * a)
        x2: float = (-b - sqrt(delta)) / (2 * a)

        print("方程有两个实数根 x1 x2: ")
        print(f"    x1 = {x1:.2f}")
        print(f"    x2 = {x2:.2f}")
    elif delta == 0:
        x: float = -b / (2 * a)
        print("方程有一个实数根 x: ")
        print(f"    x = {x:.2f}")
    else:
        print("Delta < 0 方程无实数根")
