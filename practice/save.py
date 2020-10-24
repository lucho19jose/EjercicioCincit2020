
A = [9 , 2, 10, 4, 6]
C = 0
for i in range(len(A)):
  for j in range(len(A)):
    if A[i] >= A[j]:
      if A[i] >= C:
        C = A[i]
print(C)