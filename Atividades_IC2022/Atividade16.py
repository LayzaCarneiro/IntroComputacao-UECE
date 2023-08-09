import matplotlib.pyplot as plt
# 4. [0,5p] Sejam LP1 e LP2 duas listas de pontos do plano dados pelas suas coordenadas. Por exemplo, LP1 poderia ser
#    LP1 = [[3.2, 4.5], [2.0, 4.1], [3, 6], [9.0, 7.3]] e LP2 = [[2.1, 3], [3.3, 5.4], [8, 1], [1.1, 5.5]].  Escreva uma função Python que encontra o
#    melhor casamento entre os pontos. O melhor casamento é aquele com a menor soma das distâncias entre os pares de pontos.
def casamento(LP1,LP2):
    distancia = 0
    L = []
    soma = 0
    for i in LP1:
        D1 = 10000000000
        for j in LP2:
            distancia = (((i[0]-j[0])**2) + ((i[1]-j[1])**2))**0.5
            if distancia < D1:
                D1 = distancia
        L.append(D1)
    for i in L:
        soma += i
    return soma

LP1 = [[3.2, 4.5], [2.0, 4.1], [3, 6], [9.0, 7.3]]
LP2 = [[2.1, 3], [3.3,5.4], [8, 1], [1.1, 5.5]]

print('O melhor casamento de LP1 e LP2 é {}'.format(casamento(LP1, LP2)))








