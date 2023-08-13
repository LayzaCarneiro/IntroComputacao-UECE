# Questão 6
# Escreva um programa em Python para criar um dicionário a partir de uma string. As chaves são os caracteres e os valores são as posições
# da primeira ocorrência de cada caractere.

string = str(input('Digite algo: ')).strip().lower()
L = list(string)
dados = {'a': '', 'b': '', 'c': '', 'd': '', 'e': '', 'f': '', 'g': '', 'h': '', 'i': '', 'j': '', 'k': '', 'l': '', 'm': '', 'n': '', 'o': '', 'p': '', 'q': '', 'r': '', 's': '', 't': '', 'u': '', 'v': '', 'w': '', 'x': '', 'y': '', 'z': ''}

for key, value in dados.items():
    for j in range(len(L)):
        if key == L[j]:
            dados[key] = string.find(L[j])
print(dados)