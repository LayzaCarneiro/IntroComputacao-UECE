# 2. Utilizando a representação de array da questão 2, escreva uma função matMult(M,N) que retorna o produto de M por N. A função deve verificar se o produto é possível,
#    ou seja, se o número de colunas de M é igual ao número de linhas de N. Se não for, deve retornar uma mensagem de erro.

def getLinha(matriz, n):
    return [i for i in matriz[n]]

def getColuna(matriz, n):
    return [i[n] for i in matriz]

def matMulti(mat1, mat2):
    linhas1 = len(mat1)
    colunas1 = len(mat1[0])
    linhas2 = len(mat2)
    colunas2 = len(mat2[0])
    matRes = []
    if colunas1 == linhas2:
        for i in range(linhas1):
            matRes.append([])
            for j in range(colunas2):
                listMult = [x*y for x, y in zip(getLinha(mat1, i), getColuna(mat2, j))]
                matRes[i].append(sum(listMult))
        return matRes
    else:
        print('Não é possível multiplicar as duas matrizes.')
        

MatrizA = [[2, 3, 1], [-1, 0, 2]]
MatrizB = [[1, -2], [0, 5], [4, 1]]
multiplicacao = matMulti(MatrizA, MatrizB)
for i in range(len(multiplicacao)):
    print(multiplicacao[i])