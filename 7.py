A = [0] * 6
print("Introduce 6 tiempos de respuesta (ms):")
for i in range(6):
    A[i] = int(input(f"Tiempo {i+1}: "))

max = A[0]
min = A[0]
suma = 0

for i in range(6):
    if A[i] > max:
        max = A[i]
    if A[i] < min:
        min = A[i]
    suma += A[i]

promedio = suma / 6

print("\n--- Reporte de Latencia ---")
print("Pico de latencia (Máximo):", max, "ms")
print("Tiempo de respuesta más bajo (Mínimo):", min, "ms")
print("Promedio de respuesta:", promedio, "ms")
