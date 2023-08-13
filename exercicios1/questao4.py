# Questão 4

num = int(input('Digite um número: '))
L = []
n = num

while n > 0:
    resto = n%2
    binario = resto
    n = n//2
    L.insert(0, binario)

resul = "".join(map(str, L))

print('O valor {} em binário é {}.'.format(num, resul))