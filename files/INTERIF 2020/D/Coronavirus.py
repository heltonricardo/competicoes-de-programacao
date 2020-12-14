livres, ocupados = [int(x) for x in input().split()]
f1 = f2 = f3 = f4 = 0
while True:
   entrou, saiu = [int(x) for x in input().split()]
   if entrou == saiu == 0: break
   
   q = ocupados + entrou - saiu
   p = q * 100 / livres

   ocupados += entrou - saiu

   if p < 60: f4 += 1
   elif p < 70: f3 += 1
   elif p <=80: f2 += 1
   else: f1 += 1

print('Fase 1:', f1, 'semana(s)')
print('Fase 2:', f2, 'semana(s)')
print('Fase 3:', f3, 'semana(s)')
print('Fase 4:', f4, 'semana(s)')
