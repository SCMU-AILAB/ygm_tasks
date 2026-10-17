"""
题目：一元二次函数的数学分析
给定二次函数：

f(x)=ax^2+bx+c, a != 0

程序需要实现以下数学功能：
1. 计算判别式
2. 根据判别式求出方程的实数根
3. 计算抛物线顶点坐标与对称轴
4. 计算指定自变量对应的函数值
5. 求函数在指定闭区间上的最大值和最小值
"""

import Integrate
from CalculateFuctionValue import CalculateFuctionValue
from Delta import delta
from GetCoefficients import get_coefficients
from GetEndpoints import GetEndpoints
from Integrate import integrate
from MaxValue import MaxValue
from OpeningDirection import OpeningDirection
from vertex import vertex


def main() -> None:
    a, b, c = get_coefficients()

    delta(a, b, c)

    vertex_x, vertex_y = vertex(a, b, c)

    OpeningDirection(a)

    # 可以在这里加入输入 x 值
    for x in [-2, -1, 0, 1, 2]:
        CalculateFuctionValue(a, b, c, x)

    left, right = GetEndpoints()

    MaxValue(left, right, a, b, c, vertex_x, vertex_y)

    result = integrate(a, b, c, left, right)
    print(f"此区间内函数的积分是：: {result:.2f}")


if __name__ == "__main__":
    main()
