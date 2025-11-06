
# Ejercicio 2 (map): Convertir grados Celsius a Fahrenheit



celsius = [0, 10, 20, 30]

# Conversión: F = (C * 9/5) + 32
fahrenheit = list(map(lambda c: (c * 9 / 5) + 32, celsius))

# Programa principal
if __name__ == "__main__":
    print("=== Conversión de Celsius a Fahrenheit ===")
    for c, f in zip(celsius, fahrenheit):
        print(f"{c}°C = {f}°F")
