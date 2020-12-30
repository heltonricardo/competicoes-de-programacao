d, m, a = [int(x) for x in input().split()]
t = (d % 5) + 3

mat = []
for i in range(t): mat.append([0 for x in range(t)])

mat[0][0] = a
mat[0][1] = m
mat[1][0] = d

p = 2
for i in range(2, t):
   mat[0][i] = mat[0][i-1] + p
   mat[i][0] = mat[i-1][0] + p
   p += 1

for i in range(1, t):
   for j in range(1, t):
      mat[i][j] = mat[i-1][j] + mat[i][j-1] + mat[i-1][j-1]

print(mat[t-1][t-1])
