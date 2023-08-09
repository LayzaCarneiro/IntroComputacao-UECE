#Exercício 22
'''nome = str(input('Digite seu nome completo: ')).strip()
L = nome.split()

print('Analisando seu nome...')
print('Seu nome em letras maiúsculas é', nome.upper())
print('Seu nome em letras minúsculas é', nome.lower())
print('Seu nome tem ao todo {} letras.'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome é {} e ele tem {} letras.'.format(L[0], len(L[0])))'''


#Exercício 23
'''num = int(input('Informe um número: '))
unidade = (num//1) % 10
dezena = (num//10) % 10
centena = (num//100) % 10
milhar = (num//1000) % 10

print('Analisando o número {}.'.format(num))
print('Unidade: {}'.format(unidade))
print('Dezena: {}'.format(dezena))
print('Centena: {}'.format(centena))
print('Milhar: {}'.format(milhar))'''

#Exercício 24
'''cid = str(input('Nome da sua cidade:')).strip().lower()
print(cid[:5] == 'santo')'''

#Exercício 25
'''nome = str(input('Nome: ')).strip()
print('Seu nome tem Silva? {}'.format('silva' in nome.lower()))'''

#Execício 26
'''frase = str(input('Digite a frase:')).strip()
l = frase.lower()

print('A letra A aparece {} vezes na frase.'.format(l.count('a')))
print('A primeira letra A apareceu na posição {}'.format(l.find('a')+1))
print('A última letra A apareceu na posição {}'.format(l.rfind('a')+1))'''

#Exercício 27
nome = str(input('Digite seu nome completo: ')).strip()
L = nome.split()

print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}.'.format(L[0]))
print('Seu último nome é {}.'.format(L[len(L)-1]))