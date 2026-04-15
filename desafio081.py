lista = []
while True:
  n = int(input('Digite um número: '))
  lista.append(n)
  pergunta = str(input('Quer continuar? [S/N]')).strip().upper()[0]
  if pergunta == 'N':
    break
print('-=' * 23)
print(f'No total foram digitados {len(lista)} números.')
lista.sort(reverse=True)
print(f'Os números em ordem decrescente são {lista}DD')
if 5 in lista:
  print('O número 5 faz parte da lista.')
else:
  print('O número 5 não faz parte da lista.')
