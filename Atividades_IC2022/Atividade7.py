# Questão 1
'''R = float(input('Insira o valor do raio: '))
D = float(2*R)
C = float(2*3.14*R)
A = float(3.14*R*R)
V = float((4*3.14*(R**3))/3)

print('Diâmetro: ', D)
print('Cicunferência: ', C)
print('Área da superfície: ', A)
print('Volume da esfera: ', V)'''

# Questão 2
'''L1 = int(input('Lado 1: '))
L2 = int(input('Lado 2: '))
L3 = int(input('Lado 3: '))

if L1>(L2+L3) or L2>(L1+L3) or L3>(L1+L2):
    print('Não é triângulo')
elif L1==L2==L3:
    print('Equilátero')
elif L1==L2 or L1==L3 or L2==L3:
    print('Isósceles')
else:
    print('Escaleno')'''

# Questão 3
# Em matemática, a fórmula de Leibniz para π, que leva o nome de Gottfried Wilhelm Leibniz, estabelece que π/4 = 1 - 1/3 + 1/5 - 1/7 + 1/9 - ... .
# Escreva um programa que aceita do usuário o número de iterações a ser utilizada nesta aproximação e mostra o valor resultante.
'''n = int(input('Número de iterações desejadas: '))
calc = 0
p = 1

if n%2!=0:
    while n > 0:
        if n == 1:
            calc += 1
        elif n%2==0:
            p += 2
            calc += 1/p
        elif n%2!=0:
            p += 2
            calc += -1/p
        n -= 1
else:
    while n > 0:
        if n == 1:
            calc += 1
        elif n%2==0:
            p += 2
            calc += -1/p
        elif n%2!=0:
            p += 2
            calc += 1/p
        n -= 1

print('O cálculo aproximado de π/4 com o número de iterações desejadas ficou: {}'.format(calc))'''

# Questão 4
'''num = int(input('Digite um número: '))
L = []
n = num

while n > 0:
    resto = n%2
    binario = resto
    n = n//2
    L.insert(0, binario)

resul = "".join(map(str, L))

print('O valor {} em binário é {}.'.format(num, resul))'''
