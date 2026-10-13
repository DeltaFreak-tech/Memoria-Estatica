# Creación de una matriz 3x3 dinamica
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Recorrido clasico por índices
# len(matriz)=número de filas(3), len(matriz[0])=Numero de elementos en la fila 1 (3)
for f in range(len(matriz)):
    for c in range(len(matriz[0])):
        print(f"Posición [{f},{c}]: {matriz[f][c]}")
