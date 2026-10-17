def vertex(a, b, c):
    vertex_x: float = -b / (2 * a)
    vertex_y: float = a * vertex_x**2 + b * vertex_x + c
    print(f"顶点坐标：({vertex_x:.2f}, {vertex_y:.2f})")
    print(f"对称轴：x = {vertex_x:.2f}")
    return vertex_x, vertex_y
