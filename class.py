from math import sqrt


class QuadraticFunction:
    def __init__(self, a: float, b: float, c: float):
        self.a = a
        self.b = b
        self.c = c


def delta(f: QuadraticFunction) -> float:
    return f.b * f.b - 4.0 * f.a * f.c


def roots(f: QuadraticFunction) -> tuple[int, float, float]:
    d = delta(f)

    if d > 0:
        x1 = (-f.b + sqrt(d)) / (2.0 * f.a)
        x2 = (-f.b - sqrt(d)) / (2.0 * f.a)
        return 2, x1, x2

    elif d == 0:
        x = -f.b / (2.0 * f.a)
        return 1, x, 0.0

    else:
        return 0, 0.0, 0.0


def calculate(f: QuadraticFunction, x: float) -> float:
    return f.a * x * x + f.b * x + f.c


def vertex(f: QuadraticFunction) -> tuple[float, float]:
    x = -f.b / (2.0 * f.a)
    y = calculate(f, x)
    return x, y


def axis(f: QuadraticFunction) -> float:
    return -f.b / (2.0 * f.a)


def direction(f: QuadraticFunction) -> str:
    if f.a > 0:
        return "向上"
    else:
        return "向下"


def extrema(f: QuadraticFunction,
            left: float,
            right: float) -> tuple[float, float]:

    if left > right:
        temp = left
        left = right
        right = temp

    max_value = calculate(f, left)
    min_value = max_value

    value = calculate(f, right)

    if value > max_value:
        max_value = value

    if value < min_value:
        min_value = value

    vertex_x, vertex_y = vertex(f)

    if left <= vertex_x and vertex_x <= right:
        if vertex_y > max_value:
            max_value = vertex_y

        if vertex_y < min_value:
            min_value = vertex_y

    return max_value, min_value


def mian() -> None: ## 面
    a = float(input("输入 a: "))
    b = float(input("输入 b: "))
    c = float(input("输入 c: "))

    if a == 0:
        print("a 不能为 0")
        return

    f = QuadraticFunction(a, b, c)

    print("判别式 Delta = %.2f" % delta(f))

    root_count, x1, x2 = roots(f)

    if root_count == 0:
        print("方程无实数根")

    elif root_count == 1:
        print("方程有一个实数根：%.2f" % x1)

    else:
        print("x1 = %.2f" % x1)
        print("x2 = %.2f" % x2)

    vertex_x, vertex_y = vertex(f)

    print("顶点坐标：(%.2f, %.2f)" % (vertex_x, vertex_y))
    print("对称轴：x = %.2f" % axis(f))
    print("抛物线开口%s" % direction(f))

    x = -2

    while x <= 2:
        print("f(%d) = %.4f" % (x, calculate(f, x)))
        x += 1

    left = float(input("请输入区间左端点："))
    right = float(input("请输入区间右端点："))

    max_value, min_value = extrema(f, left, right)

    if left > right:
        temp = left
        left = right
        right = temp

    print("区间：[%.2f, %.2f]" % (left, right))
    print("最大值：%.2f" % max_value)
    print("最小值：%.2f" % min_value)


if __name__ == "__mian__":
    mian()
