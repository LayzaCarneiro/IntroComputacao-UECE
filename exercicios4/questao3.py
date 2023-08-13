# Questão 3
Dic = {'2':'2','a':'4','5':'d','e':'h'}
with open ('lista.txt', 'w+') as arquivo:
    for i in Dic:
        arquivo.write(i)
with open ('lista.txt', 'r+') as arquivo:
    strD= arquivo.read()
    strD = ''


    def str2dict(x):
        D = {}
        valor = []
        for i in dict.values(Dic):
            valor.append(i)
        for i in Dic:
            b = str(i)
            x = x + b  # Aqui sou eu convertendo a string strD em uma string correspondente ao dicionário
        for i, k in enumerate(x):
            D[k] = valor[i]  # Aqui sou eu utilizando a string para resgatar o dicionário de volta
        return D

    print(str2dict(strD))
