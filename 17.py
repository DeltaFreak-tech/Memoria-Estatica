import random


class MatrizDinamica:
    def __init__(self, filas: int, columnas: int):
        self.filas = filas
        self.columnas = columnas
        self.matriz = []

    def llenar_matriz(self):
        for f in range(self.filas):
            fila_temporal = []
            for c in range(self.columnas):
                numero = random.randint(0, 9)
                fila_temporal.append(numero)
            self.matriz.append(fila_temporal)

    def mostrar_matriz(self):
        for f in range(self.filas):
            for c in range(self.columnas):
                print(f"{self.matriz[f][c]}\t", end="")
            print()

    def promedio(self):
        total = 0
        cantidad = self.filas * self.columnas
        for fila in self.matriz:
            for valor in fila:
                total += valor
        return total / cantidad


def ejecutar_ejemplo_aleatorio():
    print("=== MATRIZ ALEATORIA ===")
    f = int(input("Escriba un numero de filas: "))
    c = int(input("Escriba un numero de columnas: "))

    mi_matriz = MatrizDinamica(f, c)
    mi_matriz.llenar_matriz()

    print("\nMatriz Generada:")
    mi_matriz.mostrar_matriz()

    print(f"\nPromedio = {mi_matriz.promedio()}")


if __name__ == "__main__":
    ejecutar_ejemplo_aleatorio()
