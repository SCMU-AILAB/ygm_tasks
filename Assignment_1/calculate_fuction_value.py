def calculat_function_value(a: float, b: float, c: float, x: float):
    for x in [-2, -1, 0, 1, 2]:
        y = a * x**2 + b * x + c
        print(f"f({x}) = {y:.4f}")
    return y
