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
                numero = random.randint(0, 5)
                fila_temporal.append(numero)
            self.matriz.append(fila_temporal)

    def mostrar_matriz(self):
        for f in range(self.filas):
            for c in range(self.columnas):
                print(f"{self.matriz[f][c]}\t", end="")
            print()

    def contar_fuera_linea(self):
        contador = 0
        for f in range(self.filas):
            for c in range(self.columnas):
                if self.matriz[f][c] == 0:
                    contador += 1
        return contador


def ejecutar_monitoreo_nodos():
    print("=== CONFIGURACIÓN DEL PANEL ===")
    f = int(input("Ingrese el número de filas: "))
    c = int(input("Ingrese el número de columnas: "))

    mi_matriz = MatrizDinamica(f, c)
    mi_matriz.llenar_matriz()

    print("\n--- Estado del Panel de Nodos ---")
    mi_matriz.mostrar_matriz()

    fuera_linea = mi_matriz.contar_fuera_linea()
    print("\n--- Diagnóstico ---")
    print(f"ALERTA: Se detectaron {fuera_linea} nodo(s) fuera de línea (valor 0).")


if __name__ == "__main__":
    ejecutar_monitoreo_nodos()
