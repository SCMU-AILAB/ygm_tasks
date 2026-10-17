def CalculateFuctionValue(a, b, c, x):
    for x in [-2, -1, 0, 1, 2]:
        y = a * x**2 + b * x + c
        print(f"f({x}) = {y:.4f}")
