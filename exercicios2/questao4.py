# Questão 4
# 4. Faça um programa que decida se duas strings lidas do teclado são palíndromas mútuas, ou seja, se uma é igual à outra quando lida de traz para frente.
#    Exemplo: amor e roma.

P1 = str(input('Digite a palavra 1: ')).strip().lower()
P2 = str(input('Digite a palavra 2: ')).strip().lower()
palavra2 = list(P2)
palavra2.reverse()
palavra2 = "".join(map(str, palavra2))

if P1 == palavra2:
    print('As palavras {} e {} são palíndromas.'.format(P1, P2))
else:
    print('As palavras {} e {} NÃO são palíndromas.'.format(P1, P2))