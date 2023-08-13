# Questão 2
l = ['a','b','c','d']
with open ('lista.txt', 'w+') as arquivo:
    for i in l:
        arquivo.write(i)
with open ('lista.txt', 'r+') as arquivo:
    l=[]
    lista= arquivo.read()
    for i in lista:
        l.append(i)
    li=l[::-1]
    print(li)
