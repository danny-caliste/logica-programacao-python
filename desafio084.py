list = []
maior = menor = 0
while True:
  nom = str(input('Nome: '))
  pes = int(input('Peso: '))
  list.append([nom, pes])
  if len(list) == 1:
    menor = maior = list [-1] [1]
  else:
    if list[-1][1] > maior:
      maior = list [-1] [1]
    if list[-1][1] < menor:
      menor = list [-1] [1]
  per = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
  if per == 'N':
    break
print('-=' * 25)
print(f'O total de pessoas cadastradas foram {len(list)} pessoas.')
print(f'O maior pesso foi de {maior}kg. Peso de', end=' ')
for p in list:
  if p[1] == maior:
    print(f'({p[0]})', end=' ')
print()
print(f'O menor pesso foi de {menor}kg. Peso de', end=' ')
for p in list:
  if p[1] == menor:
    print(f'({p[0]})', end=' ')
print('DD')
  

    
