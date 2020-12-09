e1, j1 = input().split(':')
e2, j2 = input().split(':')

a = []
for i in range(3):
   a.append(input().split())

g = ''

if   a[0][0] == a[0][1] == a[0][2]: g = a[0][0]
elif a[1][0] == a[1][1] == a[1][2]: g = a[1][0]
elif a[2][0] == a[2][1] == a[2][2]: g = a[2][0]

elif a[0][0] == a[1][0] == a[2][0]: g = a[0][0]
elif a[0][1] == a[1][1] == a[2][1]: g = a[0][1]
elif a[0][2] == a[1][2] == a[2][2]: g = a[0][2]

elif a[0][0] == a[1][1] == a[2][2]: g = a[0][0]
elif a[2][0] == a[1][1] == a[0][2]: g = a[2][0]

if g == 'X':
   if e1 == 'X': print(j1, 'Ganhou')
   else: print(j2, 'Ganhou')
elif g == 'O':
   if e1 == 'O': print(j1, 'Ganhou')
   else: print(j2, 'Ganhou')
else: print('Empatou!')
