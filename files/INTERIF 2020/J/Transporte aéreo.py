p, q = [int(x) for x in input().split()]
v = p * 498 + q * 6.35

mat = []
for i in range(2):
   mat.append(['V' for j in range(8)])

for j in range(8):
   for i in range(2):
      if p:
         mat[i][j] = 'P'
         p -= 1
      elif q > 0:
         mat[i][j] = 'C'
         q -= 100
      else: break

print('{:.2f}'.format(v))
print(*mat[0], sep='')
print(*mat[1], sep='')
