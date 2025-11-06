# Ejercicio 1 (iter): Contador del 10 al 15
numeros = list(range(10, 16))


it = iter(numeros)

print("Contador del 10 al 15")

while True:
    try:
        print(next(it))
    except StopIteration:
        break  
