
# Ejercicio 2 (yield): Genera los números impares de una listas


def filtrar_impares(lista):
    for numero in lista:
        if numero % 2 != 0:  # condición para número impar
            yield numero


if __name__ == "__main__":
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    print("=== Números impares de la lista ===")
    for n in filtrar_impares(numeros):
        print(n)
