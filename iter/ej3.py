# Ejercicio 3 (iter): Clase que devuelve lista de cuadrados sin usar iter()


class Cuadrados:
    """
    Clase que genera los cuadrados del 1 al 10.
    No usa iter(), sino un método que retorna una lista completa.
    """
    def obtener_lista(self):
        resultado = []
        for i in range(1, 11):
            resultado.append(i ** 2)
        return resultado

# Programa principal


if __name__ == "__main__":
    obj = Cuadrados()

    print("=== Cuadrados del 1 al 10 ===")
    for valor in obj.obtener_lista():
        print(valor)
