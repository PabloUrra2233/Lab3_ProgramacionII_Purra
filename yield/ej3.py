# Ejercicio 3 (yield): iterable genera cuadrados 1..10

class Cuadrados:
    def __iter__(self):
        for i in range(1, 11):
            yield i ** 2  # 1, 4, 9, 16, ..., 100


if __name__ == "__main__":
    print("=== Cuadrados del 1 al 10 ===")
    for valor in Cuadrados():
        print(valor)
