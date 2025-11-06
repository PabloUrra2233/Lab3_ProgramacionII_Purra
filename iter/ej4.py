
# Ejercicio 4 (iter): Iterador que devuelve cadenas en mayúsculas


class Mayusculas:

    def __init__(self, palabras):
        self.palabras = palabras
        self.indice = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.indice < len(self.palabras):
            palabra = self.palabras[self.indice].upper()
            self.indice += 1
            return palabra
        else:
            raise StopIteration

# Programa principal
if __name__ == "__main__":
    palabras = ["python", "java", "ruby", "go"]
    print("=== Palabras en mayúsculas ===")
    for p in Mayusculas(palabras):
        print(p)
