# Questão 3
# 3. Escrever um programa que ler do teclado uma string que representa uma cadeia de DNA e gera a cadeia complementar.
# Exemplo: Entrada: AATCTGCAC, Saída: TTAGACGTG.

entrada = str(input('Informe a cadeia de DNA: ')).strip().upper()
L = []
i = len(entrada)-1
saida = str()
comp = str()

for i in range(len(entrada)):
    if entrada[i] == 'A':
        comp = 'T'
    elif entrada[i] == 'T':
        comp = 'A'
    elif entrada[i] == 'C':
        comp = 'G'
    elif entrada[i] == 'G':
        comp = 'C'
    L.append(comp)

final = "".join(map(str, L))
print('O complemento da cadeia {} é {}.'.format(entrada, final))