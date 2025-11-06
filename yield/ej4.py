# Ejercicio 4: Fibonachi hasta el décimo elemento

def fibonacci(n=10):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Programa principal
if __name__ == "__main__":
    print("=== Fibonacci (10 elementos) ===")
    for num in fibonacci(10):
        print(num)
