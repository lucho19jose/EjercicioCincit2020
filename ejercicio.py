#
tam = int(input('ingrese:'))
A = []
B = []
C = []
D = []
Dic = {}
for i in range(tam):
  b = 0
  B.clear()
  A.append(int(input('ingrese a: ')))
  b = str(input('ingrese b:'))
  for j in range(A[i]):
    B.append(b)
  C.append(int("".join(B))) 
  Dic[C[i]] = i+1

print(A)
print(C)
print(Dic)

keys = list(Dic.keys())
keys.sort()

for k in keys:
  print(Dic[k])

