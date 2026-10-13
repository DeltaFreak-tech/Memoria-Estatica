nombres = ["Juan", "María", "Pedro", "Ana"]
print("Estado inicial de la cola:", nombres)

nombres.insert(0, "Carlos")
print("Tras recibir emergencia:", nombres)

nombres.remove("Pedro")
print("Tras cancelación del nombre Pedro:", nombres)

nombres.sort()
print("Cola ordenada por prioridad:", nombres)

print("---Atención---")
print("Atendiendo cliente:", nombres[0])
nombres.pop(0)
print("Cola pendiente actualizada:", nombres)
