tickets = [105, 102, 108, 101]
print("Estado inicial de la cola:", tickets)


tickets.insert(0, 999)
print("Tras recibir emergencia:", tickets)

tickets.remove(108)
print("Tras cancelación del ticket 108:", tickets)

tickets.sort(reverse=True)
print("Cola ordenada por prioridad:", tickets)

print("---Atención---")
print("Atendiendo ticket ID:", tickets[0])
tickets.pop(0)
print("Cola pendiente actualizada:", tickets)
