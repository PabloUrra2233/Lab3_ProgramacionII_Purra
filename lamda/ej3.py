
# Ejercicio 3 (lambda): Devolver el primer elemento de una lista


primer_elemento = lambda lista: lista[0] if lista else None

# Programa principal
if __name__ == "__main__":
    frutas = ["manzana", "pera", "uva", "plátano"]
    print("=== Primer elemento de una lista ===")
    print(f"La primera fruta es: {primer_elemento(frutas)}")
