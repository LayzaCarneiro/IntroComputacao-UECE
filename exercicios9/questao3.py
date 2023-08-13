# Questão 3

def medirpalavra(P1, P2):
    P1 = list(P1)
    P2 = list(P2)
    count1 = 0
    count2 = 0
    for i in range(len(P1)-len(P2)):
        P2.append('0')
    for i in range(len(P2)-len(P1)):
        P1.append('0')
    for i in range(len(P1)):
        if P1[i] != P2[i]:
            count1 += 1
    for i in range(len(P2)):
        if P2[i] != P1[i]:
            count2 += 1
    if count1 < count2:
        return('É menor transformar P1 para P2. A distânica é {}.'.format(count1))
    elif count2 < count1:
        return('É menor transformar P2 para P1. A distânica é {}.'.format(count2))
    else:
        return('A distância é {}.'.format(count1))

palavra1 = input('Palavra 1: ').lower().strip()
palavra2 = input('Palavra 2: ').lower().strip()

print(medirpalavra(palavra1, palavra2))