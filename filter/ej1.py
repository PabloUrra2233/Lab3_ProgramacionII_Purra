
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


pares = list(filter(lambda x: x % 2 == 0, numeros))

# Programa principal
if __name__ == "__main__":
    print("=== Números pares ===")
    print(f"Lista original: {numeros}")
    print(f"Pares:          {pares}")
