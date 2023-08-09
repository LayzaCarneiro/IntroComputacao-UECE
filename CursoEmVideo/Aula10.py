from random import randint
from time import sleep
from datetime import date

#Exercício 28
'''print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)

L = randint(0, 5)
num = int(input('Em que número pensei?'))

print('PROCESSANDO...')
sleep(2)

if L == num:
    print('PARABÉNS! Você conseguiu me vencer! ;)')
else:
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(L, num))'''

#Exerício 29
'''vel = float(input('Qual a velocidade atual do carro?'))
multa = 7*(vel-80)

if vel > 80:
    print('MULTADO! Você excedeu o limite permitido que é de 80km/h')
    print('Você deve pagar uma multa de R${:.2f}!'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')'''

#Exercício 30
'''num = int(input('Me diga um número qualquer:'))
if num%2==0:
    print('O número {} é PAR.'.format(num))
else:
    print('O número {} é ÍMPAR.'.format(num))'''

#Exercício 31
'''dist = float(input('Qual é a distância da sua viagem?'))
print('Você está prestes a começar uma viagem de {}km.'.format(dist))

preço = dist * 0.5 if dist <= 200 else dist * 0.45

print('E o preço da sua passagem será de R${:.2f}.'.format(preço))'''

#Exercício 32
'''ano = int(input('Que ano quer analisar? Colo que 0 para analisar o ano atual: '))

if ano == 0:
    ano = date.today().year
if ano%4 == 0 and ano%100 != 0 or ano%400 == 0:
    print('O ano {} é bissexto.'.format(ano))
else:
    print('O ano {} não é bissexto.'.format(ano))'''

#Exercício 33
'''num1 = float(input('Primeiro valor:'))
num2 = float(input('Segundo valor:'))
num3 = float(input('Terceiro valor:'))

menornum = num1
maiornum = num3

if num2 < num1 and num2 < num3:
    menornum = num2
elif num3 < num2 and num3 < num1:
    menornum = num3
if num1 > num2 and num1 > num3:
        maiornum = num1
elif num2 > num1 and num2 > num3:
        maiornum = num2

print('O menor valor digitado foi {:.0f}.'.format(menornum))
print('O maior valor digitado foi {:.0f}.'.format(maiornum))'''

#Exercício 34
'''salario = float(input('Qual é o salário do funcionário? R$'))

if salario > 1250:
    aum = salario + (0.1*salario)
else:
    aum = salario + (0.15*salario)
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(salario, aum))'''

#Exercício 35
print("-="*20)
print("Analisador de Triângulos")
print("-="*20)
l1 = float(input('Primeiro segmento: '))
l2 = float(input('Segundo segmento: '))
l3 = float(input('Terceiro segmento: '))

if l1>(l2+l3) or l2>(l1+l3) or l3>(l1+l2):
    print('Os segmentos acima NÃO PODEM FORMAR triângulo!')
else:
    print('Os segmentos acima PODEM FORMAR triângulo!')