def maxvalue(left, right, a, b, c, vertex_x, vertex_y):
    if left > right:
        left, right = right, left

    y_left = a * left**2 + b * left + c
    y_right = a * right**2 + b * right + c

    values = [y_left, y_right]

    if left <= vertex_x <= right:
        values.append(vertex_y)

    max_value = max(values)
    min_value = min(values)
    print(f"区间：[{left}, {right}]")
    print(f"最大值：{max_value:.2f}")
    print(f"最小值：{min_value:.2f}")
