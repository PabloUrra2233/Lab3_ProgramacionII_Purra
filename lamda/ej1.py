
# Ejercicio 1 (lambda): Retornar el mayor de dos números



mayor = lambda x, y: x if x > y else y

# Programa principal
if __name__ == "__main__":
    print("=== Comparar dos números ===")
    a, b = 15, 9
    print(f"Entre {a} y {b}, el mayor es: {mayor(a, b)}")
