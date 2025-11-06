
from functools import reduce


numeros = [7, 3, 9, 1, 5]

mayor = reduce(lambda x, y: x if x > y else y, numeros)


if __name__ == "__main__":
    print("=== Número mayor de la lista ===")
    print(f"Lista: {numeros}")
    print(f"Mayor: {mayor}")
