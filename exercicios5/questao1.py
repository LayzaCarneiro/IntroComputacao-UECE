# 1. Python básico não define o tipo de dado array (matriz). Uma matriz em Python pode ser construída como uma lista de linhas onde cada linha é uma lista,
#    ou seja, uma lista de listas. Exemplos: A = [[2, 4.1, 3], [1, 1, 1], [2.0, 4.3, 9]], B = [[2.2, 4], [5, 6], [9, 2.0]], C = [[5, 6.8, 4], [3, 1, 2.1]],
#    D = [[2, 3, 3.3], [4.2, 3.1]]. Nesse caso, A é uma matriz 3x3, B é uma matriz 3x2, C é uma matriz 2x3 e D não é uma matriz. Escreva e teste uma função matTransp(M)
#    que retorna a transposta de uma matriz M. A função deve verificar se M é mesmo uma matriz e retornar uma mensagem de erro se não for.

A = [[2, 3, 3.3], [4.2, 3.1]]

def matTransp(M):
    for i in range(1, len(M)):
        if len(M[0]) == len(M[i]):
            linhas = len(M)
            colunas = len(M[0])
            transposta = [[0 for i in range (linhas)] for i in range (colunas)]
            for i in range(linhas):
                for j in range(colunas):
                    transposta[j][i] = M[i][j]
            return transposta
        else:
            print('NÃO É UMA MATRIZ.')

transposta = matTransp(A)
for i in range(len(transposta)):
    print(transposta[i])