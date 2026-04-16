lista = list()
pares = []
ímpares = []
while True:
  n = int(input('Digite um número: '))
  lista.append(n)
  p = str(input('Quer contínuar? [S/N] ')).strip().upper()[0]
  if p == 'N':
    break
for c in lista:
  if c % 2 == 0:
      pares.append(c)
   else:
      ímpares.append(c)
  print('-=' * 25)
  print(f'A lista completa é {lista}')
  print(f'A lista pares é {pares}DD')
  print(f'A lista ímpares é {ímpares}')
    
