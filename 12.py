valores = [8, 2, 12, 45, 43, 67]

num = int(input("Ingresa un valor: "))

print("Valores del arreglo:")
for i in range(6):
    print(valores[i])

for i in range(6):
    valores[i] = valores[i] * num

print("\nValores del arreglo multiplicados por", num, ":")
for i in range(6):
    print(valores[i])
