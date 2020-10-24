
cantidad = int(input('cantidad: '))
i = 0
entradas = []
while i < cantidad:
  entradas.append(input('ingrese el primer valor'))
  i += 1 
joinx = int(''.join(entradas))
print(joinx)