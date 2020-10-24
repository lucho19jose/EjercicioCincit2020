lista = []
for letra in 'casa':
  lista.append(letra)
list2 = [letra for letra in 'casa']

print(list2)

list4 = [ numero**2 for numero in [ numero for numero in range(1,11) if numero % 4 == 0 ] if numero % 2 == 0]
print(list4)