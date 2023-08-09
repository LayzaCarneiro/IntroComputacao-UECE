#Questão 1
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

#Usuário
#num = float(input('Número que deseja calcular a raiz: '))
#erro = float(input('Erro máximo tolerável: '))
#print(raiz(num, erro))

#Questão 2
def ordenar(L):
    L1 = L
    L2 = []
    L2.append(L1[0])
    for i in L1:
        if i == L2[0]:
            L2 = L2
        elif i > L2[len(L2)-1]:
            L2.append(i)
        else:
            for n in range (0, (len(L2))):
                if i < L2[n]:
                    L2.insert(n, i)
                    break

    return(L2)

L1 = [12, 25, 1, 74, 90, 7, 102, 0.5, 24]
L2 = [0.8, 33, 21, 150, 0.01]
L3 = [1002, 4, 710, 0.2, 2.4, 3000]

print('L1: ', ordenar(L1))
print('L2: ', ordenar(L2))
print('L3: ', ordenar(L3))