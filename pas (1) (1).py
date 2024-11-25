print("santiago vazquez cruz, Aldo hernandez guerrero")
def pascal_triangle(n):
    """Genera el triángulo de Pascal hasta la fila n."""
    triangle = []
    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)
    return triangle
def print_triangle(triangle):
    """Imprime el triángulo de Pascal."""
    for row in triangle:
        print(" ".join(map(str, row)))
n = int(input("Introduce el número de filas: "))
triangle = pascal_triangle(n)
print_triangle(triangle)
