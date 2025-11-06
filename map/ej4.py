
# Ejercicio 4 (map): Calcular el cuadrado de cada número


# Lista original
numeros = [1, 2, 3, 4, 5]

# Aplicamos map() para obtener los cuadrados
cuadrados = list(map(lambda x: x ** 2, numeros))

# Programa principal
if __name__ == "__main__":
    print("=== Cuadrados de los números ===")
    print(f"Lista original: {numeros}")
    print(f"Cuadrados:      {cuadrados}")
