def integrate(a, b, c, left, right):
    def F(x):
        return a * x**3 / 3 + b * x**2 / 2 + c * x

    return F(right) - F(left)
