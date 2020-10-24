#entender listas

A = [ i**2 for i in [j for j in range(10) if j % 2 != 0] ]
print(A)