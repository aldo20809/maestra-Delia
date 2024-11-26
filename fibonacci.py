print("hecho por santiago y aldo")
def fibonacci(n):
    # Lista para almacenar la serie
    serie = [0, 1]  
    for i in range(2, n):
        # Agregar el siguiente número sumando los dos anteriores
        serie.append(serie[-1] + serie[-2])
    return serie[:n]  # Retorna los primeros 'n' términos

# Ejemplo de uso
n = 10  # Cambia este valor para generar más términos
print(f"Los primeros {n} términos de la serie de Fibonacci son: {fibonacci(n)}")