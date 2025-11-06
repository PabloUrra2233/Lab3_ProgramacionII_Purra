
# Lista de palabras
animales = ["perro", "gato", "pato", "hamster"]

# Filtramos las que comienzan con 'p'
empiezan_con_p = list(filter(lambda palabra: palabra.startswith("p"), animales))

# Programa principal
if __name__ == "__main__":
    print("=== Palabras que comienzan con 'p' ===")
    print(f"Lista original: {animales}")
    print(f"Filtradas:      {empiezan_con_p}")
