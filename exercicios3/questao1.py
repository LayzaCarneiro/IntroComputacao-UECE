# 1. Escreva um programa que lê duas strings. Se as strings são anagramas uma da outra, retorna "Verdadeiro". Se não, reforna "Falso". Duas palavras são anagramas
#    se uma é um rearranjo das letras da outra.

pri = input('Primeira string: ').lower().strip()
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
print(resp)