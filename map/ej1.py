
# Ejercicio 1 (map): Multiplicar cada número por 10



numeros = [1, 2, 3, 4, 5]

multiplicados = list(map(lambda x: x * 10, numeros))

# Programa principal
if __name__ == "__main__":
    print("=== Números multiplicados por 10 ===")
    print(f"Lista original: {numeros}")
    print(f"Lista nueva:    {multiplicados}")
