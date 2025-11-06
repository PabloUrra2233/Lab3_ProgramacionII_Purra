
# Ejercicio 2 (lambda): Longitud de una cadena



longitud = lambda cadena: len(cadena)


if __name__ == "__main__":
    texto = "Programación"
    print("=== Longitud de una cadena ===")
    print(f"La palabra '{texto}' tiene {longitud(texto)} caracteres.")
