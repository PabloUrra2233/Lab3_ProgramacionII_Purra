# Ejercicio 2 (iter): impares del 1 al 20 usando yield en una calase

class Impares:
    def __iter__(self):
        for i in range(1, 21):
            if i % 2 != 0:
                yield i


if __name__ == "__main__":

    print("=== Números impares del 1 al 20 ===")
    
    for num in Impares():
        print(num)
