pilha = []
p = str(input('Digite uma conta: '))
for c in p:
  if c == '(':
    pilha.append('(')
  elif c == ')':
    if len(pilha) > 0:
      pilha.pop()
    else:
      pilha.append(')')
if len(pilha) == 0:
  print('Sintaxi correta.')
else:
  print('Sintaxe incorreta.DD')
