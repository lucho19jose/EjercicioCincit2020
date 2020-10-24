#
tam = int(input('ingrese:'))
A = []#se almacena a
B = []#lista temporal que nos permite join
C = []#lista principal
Dic = {}# se guarda el indice del C y el valor de C
#ingresando valores
for i in range(tam):
  b = 0
  B.clear()
  A.append(int(input('ingrese a: ')))
  b = str(input('ingrese b:'))
  for j in range(A[i]):
    B.append(b)
  C.append(int("".join(B))) 
  Dic[C[i]] = i+1 #Dic save

print(C)
#Logica de ordenamiento
keys = list(Dic.keys())
keys.sort()

rsta = [] 

for k in keys:
  rsta.append(Dic[k])

print(rsta)
