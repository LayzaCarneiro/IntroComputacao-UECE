# 4. Escreva um programa para encontrar o maior e o segundo maior elemento em uma lista
#    de elementos. Imprima o par posição-valor.

valor1 = int(input('Digite um valor para a posição 0: '))
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
print('E o segundo maior valor está na posição {}, e foi o valor {}.'.format(pos2, maior2))