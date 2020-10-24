text = input()

listtext = list(text)
mit = int(len(listtext)/2) + 1
listmen = listtext[mit:]

long = len(listtext)
for x,i in enumerate(listtext):
  if listtext[x] == '(':
    k = 0
    j = x
    while j < len(listtext):
      if listtext[j] == ')':
        listtext[j] = '.'
        break
      else:
        if (j + 1) == long:
          k += 1
          break
      j += 1
  
if(k == 1):
  print('no')
else:
  print('si')

