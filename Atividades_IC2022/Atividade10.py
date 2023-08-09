# 1. Escreva um programa que lê duas strings. Se as strings são anagramas uma da outra, retorna "Verdadeiro". Se não, reforna "Falso". Duas palavras são anagramas
#    se uma é um rearranjo das letras da outra.
'''pri = input('Primeira string: ').lower().strip()
seg = input('Segunda string: ').lower().strip()
lista1 = list(pri)
lista1.sort()
lista2 = list(seg)
lista2.sort()

for i in range(len(pri)):
    if len(pri)==len(seg):
        if lista1[i]==lista2[i]:
            resp = 'São anagramas.'
        else:
            resp = 'NÃO são anagramas.'
print(resp)'''

#2. Escreva um programa que lê dia, mês e ano como números e o dia da semana como
# D23456S e escreve por extenso. Por exemplo:
# Entre com o dia >>> 28
# Entre com o mês >>> 9
# Entre com o ano >>> 2022
# Entre com o dia da semana >>> S
# Saída: A data é: : Sábado, 28 de setembro de 2022.
'''dia = (input('Entre com o dia: '))
mes = (input('Entre com o mês: '))
ano = (input('Entre com o ano: '))
diasem = (input('Entre com o dia da semana: '))
mes_do_ano = {'1':'Janeiro', '2':'Fevereiro', '3':'Março', '4':'Abril', '5':'Maio', '6':'Junho', '7':'Julho', '8':'Agosto', '9':'Setembro', '10':'Outubro', '11':'Novembro', '12':'Dezembro'}
dia_da_semana = {'D': 'Domingo', '2':'Segunda-feira', '3':'Terça-feira', '4':'Quarta-feira', '5':'Quinta-feira', '6':'Sexta-feira','S':'Sábado'}

print('A data é: {}, {} de {} de {}.'.format(dia_da_semana[diasem], dia, mes_do_ano[mes], ano))'''

#3. Escreva um programa que lê uma string do teclado e retorna uma tabela com as letras em ordem alfabética e o número de vezes em que a letra ocorreu.
#   Armazene a tabela em um dicionário antes de imprimir. Imprimir a tabela e o dicionário.
'''frase = input('Entre com uma frase >>>  ').lower().strip()
L = list(frase)
M =  L.sort()
P = "".join(map(str, L)).strip()

dict = {'a': '', 'b': '', 'c': '', 'd': '', 'e': '', 'f': '', 'g': '', 'h': '', 'i': '', 'j': '', 'k': '', 'l': '', 'm': '', 'n': '', 'o': '', 'p': '', 'q': '', 'r': '', 's': '', 't': '', 'u': '', 'v': '', 'w': '', 'x': '', 'y': '', 'z': ''}

for key, value in dict.items():
    for j in range(len(L)):
        if key == L[j]:
            dict[key] = frase.count(L[j])
print('Dicionário: ', dict)
print('Tabela: ')

for i in range(len(P)):
    if P.find('a') == i:
        print('a', frase.count('a'))
    if P.find('b') == i:
        print('b', frase.count('b'))
    if P.find('c') == i:
        print('c', frase.count('c'))
    if P.find('d') == i:
        print('d', frase.count('d'))
    if P.find('e') == i:
        print('e', frase.count('e'))
    if P.find('f') == i:
        print('f', frase.count('f'))
    if P.find('g') == i:
        print('g', frase.count('g'))
    if P.find('h') == i:
        print('h', frase.count('h'))
    if P.find('i') == i:
        print('i', frase.count('i'))
    if P.find('j') == i:
        print('j', frase.count('j'))
    if P.find('k') == i:
        print('k', frase.count('k'))
    if P.find('l') == i:
        print('l', frase.count('l'))
    if P.find('m') == i:
        print('m', frase.count('m'))
    if P.find('n') == i:
        print('n', frase.count('n'))
    if P.find('o') == i:
        print('o', frase.count('o'))
    if P.find('p') == i:
        print('p', frase.count('p'))
    if P.find('q') == i:
        print('q', frase.count('q'))
    if P.find('r') == i:
        print('r', frase.count('r'))
    if P.find('s') == i:
        print('s', frase.count('s'))
    if P.find('t') == i:
        print('t', frase.count('t'))
    if P.find('u') == i:
        print('u', frase.count('u'))
    if P.find('v') == i:
        print('v', frase.count('v'))
    if P.find('w') == i:
        print('w', frase.count('w'))
    if P.find('x') == i:
        print('x', frase.count('x'))
    if P.find('y') == i:
        print('y', frase.count('y'))
    if P.find('z') == i:
        print('z', frase.count('z'))'''


# 4. Escreva um programa para encontrar o maior e o segundo maior elemento em uma lista
#    de elementos. Imprima o par posição-valor.
'''valor1 = int(input('Digite um valor para a posição 0: '))
valor2 = int(input('Digite um valor para a posição 1: '))
valor3 = int(input('Digite um valor para a posição 2: '))
valor4 = int(input('Digite um valor para a posição 3: '))
valor5 = int(input('Digite um valor para a posição 4: '))
L = [valor1, valor2, valor3, valor4, valor5]
maior1 = 0
maior2 = 0

print('Os valores digitados foram: {}.'.format(L))

for i in range(0, 5):
    if L[i] > maior1:
        maior1 = L[i]
        pos1 = i
print('Dentre eles, o maior valor está na posição {}, e foi o valor {}.'.format(pos1, maior1))

for i in range(0, 5):
    if L[i] > maior2 and L[i] < maior1:
        maior2 = L[i]
        pos2 = i
print('E o segundo maior valor está na posição {}, e foi o valor {}.'.format(pos2, maior2))'''

# Questão 5
'''valores = {'Valor1': 1, 'Valor2': 2, 'Valor3': 3, 'Valor4': 4, 'Valor5': 5}
maior1 = max(valores.values())
maior2 = 0
L = []

for i in valores.items():
    L.append(i)
for i in valores.values():
    if i > maior2 and i < maior1:
        maior2 = i
for k,v in enumerate(valores.values()):
    if v == maior1:
        pos1 = k
for k, v in enumerate(valores.values()):
    if v == maior2:
        pos2 = k

print(f'O par chave-valor do maior elemento do dicionário é {L[pos1]}.')
print(f'E o par chave-valor do segundo maior elemento do dicionário é {L[pos2]}.')'''

# Questão 6
# Escreva um programa em Python para criar um dicionário a partir de uma string. As chaves são os caracteres e os valores são as posições
# da primeira ocorrência de cada caractere.
'''string = str(input('Digite algo: ')).strip().lower()
L = list(string)
dados = {'a': '', 'b': '', 'c': '', 'd': '', 'e': '', 'f': '', 'g': '', 'h': '', 'i': '', 'j': '', 'k': '', 'l': '', 'm': '', 'n': '', 'o': '', 'p': '', 'q': '', 'r': '', 's': '', 't': '', 'u': '', 'v': '', 'w': '', 'x': '', 'y': '', 'z': ''}

for key, value in dados.items():
    for j in range(len(L)):
        if key == L[j]:
            dados[key] = string.find(L[j])
print(dados)'''
