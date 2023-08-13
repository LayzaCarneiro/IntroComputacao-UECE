# Questão 3
# Em matemática, a fórmula de Leibniz para π, que leva o nome de Gottfried Wilhelm Leibniz, estabelece que π/4 = 1 - 1/3 + 1/5 - 1/7 + 1/9 - ... .
# Escreva um programa que aceita do usuário o número de iterações a ser utilizada nesta aproximação e mostra o valor resultante.

n = int(input('Número de iterações desejadas: '))
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

print('O cálculo aproximado de π/4 com o número de iterações desejadas ficou: {}'.format(calc))
