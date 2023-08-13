# Questão 1

def raiz(num, erro):
    num = num
    erro = erro
    inicio = 1
    final = num
    teste = (inicio + final) / 2

    if num >= 1:
        if num == 1.0:
            return('A raiz de 1 é 1.')
        else:
            while abs(num - teste**2) > erro:
                if (num - teste**2) > 0:
                    inicio = teste
                else:
                    final = teste
                teste = (inicio + final)/2
            return('A raiz de {} é {:.2f}.'.format(num, teste))
    elif num > 0 and num < 1:
        while abs(num - teste ** 2) > erro:
            if (num - teste ** 2) > 0:
                final = teste
            else:
                inicio = teste
            teste = (inicio + final) / 2
        return ('A raiz de {} é {}.'.format(num, teste))
    else:
        return('O número inserido tem que ser um número positivo.')

# Usuário
# num = float(input('Número que deseja calcular a raiz: '))
# erro = float(input('Erro máximo tolerável: '))
# print(raiz(num, erro))

num1 = 9
erro1 = 1
print('Teste 1:', raiz(num1, erro1))

num2 = 0.16
erro2 = 0.0002
print('Teste 2:',raiz(num2, erro2))

num3 = 4
erro3 = 0.01
print('Teste 3:',raiz(num3, erro3))

num4 = 24.5
erro4 = 0.004
print('Teste 4:',raiz(num4, erro4))

num5 = 0.25
erro5 = 0.00002
print('Teste 5:',raiz(num5, erro5))