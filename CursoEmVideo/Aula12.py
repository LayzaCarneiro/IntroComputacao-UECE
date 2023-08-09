from datetime import date
from random import randint
from time import sleep

#Exercício 37 - Conversão
'''num = int(input('Digite um número inteiro: '))
print('Escolha uma das bases para conversão: \n[ 1 ] converter para BINÁRIO \n[ 2 ] converter para OCTAL \n[ 3 ] converter para HEXADECIMAL')
opc = int(input('Sua opção: '))

if opc == 1:
    print('{} convertido para BINÁRIO é igual a {}.'.format(num, bin(num)[2:]))
elif opc == 2:
    print('{} convertido para OCTAL é igual a {}.'.format(num, oct(num)[2:]))
else:
    print('{} convertido para HEXADECIMAL é igual a {}.'.format(num, hex(num)[2:]))'''

#Exercício 39
'''atual = date.today().year
ano = int(input('Ano de nascimento: '))
idade = atual - ano
dif1 = 18 - idade
dif2 = idade - 18
print('Quem nasceu em {} tem {} anos em {}.'.format(ano, idade, atual))

if idade < 18:
    print('Ainda faltam {} anos para o seu alistamento. \nSeu alistamento será em {}.'.format(dif1, (atual + dif1)))
elif idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
else:
    print('Você já deveria ter se alistado há {} anos. \nSeu alistamendo foi em {}.'.format(dif2, (atual - dif2)))'''
