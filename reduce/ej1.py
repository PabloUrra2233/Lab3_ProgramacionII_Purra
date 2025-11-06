
from functools import reduce

# Lista original
numeros = [5, 10, 15, 20]

# Usamos reduce con una función lambda para sumar
suma_total = reduce(lambda x, y: x + y, numeros)

# Programa principal
if __name__ == "__main__":
    print("=== Suma total de la lista ===")
    print(f"Lista: {numeros}")
    print(f"Suma total: {suma_total}")
