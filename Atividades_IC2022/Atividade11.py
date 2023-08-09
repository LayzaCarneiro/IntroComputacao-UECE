# 1. Escreva uma função str2dict() que transforma uma string correspondente a um dicionário em uma variável dicionário.
#    Exemplo: Dic = {"2": 2, "a": "4", 5:"d", e:h} é um dicionário. Forme a string strD = str(Dic). A função str2dict(strD) deve recuperar o dicionário Dic.
#    Testar e mostrar o resultado em três exemplos.
Dic = {"2": 2, "a": "4", 5:"d", "e":"h"}
strD = '2ade'

def str2dict(S):
    dicionario = {}
    string = []
    for i in dict.values(Dic):
        string.append(i)
    for i in Dic:
        s = str(i)
        S = S + s
    for i, k in enumerate(S):
        dicionario[k] = string[i]
    return dicionario

print(str2dict(strD))



