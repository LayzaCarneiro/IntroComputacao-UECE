# Questão 1

D = {'Pedro Santos': [39, 'Brasil', '99993333', '9.200,00'], 'Layza Carneiro': [19, 'França', '24042003', '20.500,00'],
     'Yan Luz': [24, 'Estados Unidos', '17072017', '700.000,00'], 'Berlim': [63, 'Alemanha', '87432569', '1.000,00'],
     'Marina Rodrigues': [50, 'China', '12345678', '13,00'], 'Ibiza': [91, 'Espanha', '98127634', '120.240,00']}

print("""Opções:
[1] Nacionalidade
[2] Idade mínima
[3] Nacionalidade e idade mínima
""")
escolha = int(input('Número da sua escolha: '))

if escolha == 1:
    nacionalidade = input('Nacionalidade: ').strip().title()
    for i in D.items():
        if i[1][1] == nacionalidade:
            print(i)

elif escolha == 2:
    idade = int(input('Idade mínima: '))
    for i in D.items():
        if i[1][0] >= idade:
            print(i)

elif escolha == 3:
    nacionalidade = input('Nacionalidade: ').strip().title()
    idade = int(input('Idade mínima: '))
    for i in D.items():
        if i[1][0] >= idade:
            print(i)
        elif i[1][1] == nacionalidade:
            print(i)