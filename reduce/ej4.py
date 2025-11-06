
from functools import reduce

palabras = ["Hola", "Mundo", "!"]

frase = reduce(lambda x, y: x + " " + y, palabras)

# Programa principal
if __name__ == "__main__":
    print("=== Concatenación de cadenas ===")
    print(f"Lista: {palabras}")
    print(f"Frase final: {frase}")
