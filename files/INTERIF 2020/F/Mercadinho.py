while True:
   try: idade = int(input())
   except: break
   pontos = int(input())
   valor = float(input())

   desc = 0.0
   if pontos:
      desc = pontos * 2 + idade / 4
      valor -= (valor * desc) / 100

   print('{:.2f}'.format(valor))
   print('{:.2f}%'.format(desc))
   
