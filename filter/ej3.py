
# Lista original
numeros = [10, 60, 30, 80, 50, 100]

# Filtramos los que sean mayores a 50
mayores_a_50 = list(filter(lambda x: x > 50, numeros))

# Programa principal
if __name__ == "__main__":
    print("=== Números mayores a 50 ===")
    print(f"Lista original: {numeros}")
    print(f"Mayores a 50:   {mayores_a_50}")
