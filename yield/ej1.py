# Ejercicio 1 - Función generadora con yield
# Objetivo: debolvemos los primeros 10 números pares usando yield y recorre con un for

def generar_pares():
    """Genera los primeros 10 números pares (del 2 al 20)"""
    for i in range(1, 11):
        yield i * 2  # cada yield "pausa" la función y entrega un valor

# Recorremos el generador con un for
print("primeros 10 números pares:")
for numero in generar_pares():
    print(numero)
