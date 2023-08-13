# Questão 2
L1 = int(input('Lado 1: '))
L2 = int(input('Lado 2: '))
L3 = int(input('Lado 3: '))

if L1>(L2+L3) or L2>(L1+L3) or L3>(L1+L2):
    print('Não é triângulo')
elif L1==L2==L3:
    print('Equilátero')
elif L1==L2 or L1==L3 or L2==L3:
    print('Isósceles')
else:
    print('Escaleno')