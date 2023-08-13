# Como fiz 3 exemplos no mesmo programa, eu apenas troquei a variável Dic e strD, para não dar erro, mas a função é a mesma, 
# basta trocar o Dic no programa que a função cria uma str correspondente e resgata o dicionário

# Exemplo 1
Dic={'2':2,'a':'4',5:'d','e':'h'}
strD=''
def str2dict(x):
    D={}
    valor=[]
    for i in dict.values(Dic):
        valor.append(i)
    for i in Dic:
        b=str(i)
        x=x+b  # Aqui sou eu convertendo a string strD em uma string correspondente ao dicionário 
    for i, k in enumerate (x):
        D[k]=valor[i]      # Aqui sou eu utilizando a string para resgatar o dicionário de volta
    return D
print(str2dict(strD))

# Exemplo 2
Dic2={'4':4,'b':'a','e':'d','h':'f'}
strD2=''
def str2dict(x):
    D2={}
    valor=[]
    for i in dict.values(Dic2):
        valor.append(i)
    for i in Dic2:
        b=str(i)
        x=x+b  # Aqui sou eu convertendo a string strD2 em uma string correspondente ao dicionário 
    for i, k in enumerate (x):
        D2[k]=valor[i]      # Aqui sou eu utilizando a string para resgatar o dicionário de volta
    return D2
print(str2dict(strD2))

# Exemplo 3
Dic3={'5':4,'c':'b','d':'e'}
strD3=''
def str2dict(x):
    D3={}
    valor=[]
    for i in dict.values(Dic3):
        valor.append(i)
    for i in Dic3:
        b=str(i)
        x=x+b  # Aqui sou eu convertendo a string strD3 em uma string correspondente ao dicionário 
    for i, k in enumerate (x):
        D3[k]=valor[i]      # Aqui sou eu utilizando a string para resgatar o dicionário de volta
    return D3
print(str2dict(strD3))
