
from functools import reduce

numeros = [2, 3, 4]

producto_total = reduce(lambda x, y: x * y, numeros)

# Programa principal
if __name__ == "__main__":
    print("=== Producto total de la lista ===")
    print(f"Lista: {numeros}")
    print(f"Producto total: {producto_total}")
