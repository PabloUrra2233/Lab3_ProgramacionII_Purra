
# Ejercicio 3 (map): Obtener longitudes de palabras



palabras = ["uno", "dos", "tres"]

# Aplicamos map() para obtener la longitud de cada palabra
longitudes = list(map(lambda palabra: len(palabra), palabras))

# Programa principal
if __name__ == "__main__":
    print("=== Longitud de cada palabra ===")
    for p, l in zip(palabras, longitudes):
        print(f"'{p}' tiene {l} letras.")
