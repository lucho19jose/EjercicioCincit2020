#moda python
tam = int(input('ingrese tam: '))
A = []
B = {}
u = 0
for i in range(tam):
  A.append(input('ingrese value: '))
for x,j in enumerate(A):
  B[A[x]] = A.count(A[x])

claves = list(B.keys())
values = list(B.values())
indice = 0
mayor = 0
for k, u in enumerate(values):
  for l, w in enumerate(values):
    if values[k] >= values[l]:
      if values[k] >= mayor:
        mayor = values[k]
        indice = k

print("{} se ha repetido el valor {} ".format(mayor, claves[indice]))

