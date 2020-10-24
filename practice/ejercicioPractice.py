num = int(input('ingrese num:'))

s = 0
for i in range(num):
  if num % (i+1) == 0:
    s += 1
if s > 2:
  print('el numero no es primo')
else:
  print('el numero es primo')

print(range(num))

