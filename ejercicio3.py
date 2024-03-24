def espiral_numerico(x, y):
   
    capa = max(x, y)
    valor_base = (capa - 1) * (capa - 1) + 1
    if x <= y:
        offset = x - 1
    else:
        offset = (capa - 1) - (y - 1)

    return valor_base + offset

x = 3
y = 2
valor = espiral_numerico(x, y)
print(f"El valor del número en la posición ({x}, {y}) es: {valor}")
