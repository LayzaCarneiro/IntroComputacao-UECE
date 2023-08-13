#3. Escreva um programa que lê uma string do teclado e retorna uma tabela com as letras em ordem alfabética e o número de vezes em que a letra ocorreu.
#   Armazene a tabela em um dicionário antes de imprimir. Imprimir a tabela e o dicionário.

frase = input('Entre com uma frase >>>  ').lower().strip()
L = list(frase)
M =  L.sort()
P = "".join(map(str, L)).strip()

dict = {'a': '', 'b': '', 'c': '', 'd': '', 'e': '', 'f': '', 'g': '', 'h': '', 'i': '', 'j': '', 'k': '', 'l': '', 'm': '', 'n': '', 'o': '', 'p': '', 'q': '', 'r': '', 's': '', 't': '', 'u': '', 'v': '', 'w': '', 'x': '', 'y': '', 'z': ''}

for key, value in dict.items():
    for j in range(len(L)):
        if key == L[j]:
            dict[key] = frase.count(L[j])
print('Dicionário: ', dict)
print('Tabela: ')

for i in range(len(P)):
    if P.find('a') == i:
        print('a', frase.count('a'))
    if P.find('b') == i:
        print('b', frase.count('b'))
    if P.find('c') == i:
        print('c', frase.count('c'))
    if P.find('d') == i:
        print('d', frase.count('d'))
    if P.find('e') == i:
        print('e', frase.count('e'))
    if P.find('f') == i:
        print('f', frase.count('f'))
    if P.find('g') == i:
        print('g', frase.count('g'))
    if P.find('h') == i:
        print('h', frase.count('h'))
    if P.find('i') == i:
        print('i', frase.count('i'))
    if P.find('j') == i:
        print('j', frase.count('j'))
    if P.find('k') == i:
        print('k', frase.count('k'))
    if P.find('l') == i:
        print('l', frase.count('l'))
    if P.find('m') == i:
        print('m', frase.count('m'))
    if P.find('n') == i:
        print('n', frase.count('n'))
    if P.find('o') == i:
        print('o', frase.count('o'))
    if P.find('p') == i:
        print('p', frase.count('p'))
    if P.find('q') == i:
        print('q', frase.count('q'))
    if P.find('r') == i:
        print('r', frase.count('r'))
    if P.find('s') == i:
        print('s', frase.count('s'))
    if P.find('t') == i:
        print('t', frase.count('t'))
    if P.find('u') == i:
        print('u', frase.count('u'))
    if P.find('v') == i:
        print('v', frase.count('v'))
    if P.find('w') == i:
        print('w', frase.count('w'))
    if P.find('x') == i:
        print('x', frase.count('x'))
    if P.find('y') == i:
        print('y', frase.count('y'))
    if P.find('z') == i:
        print('z', frase.count('z'))