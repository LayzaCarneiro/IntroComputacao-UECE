# ATIVIDADE 8
# Questão 1
# 1. Ler o nome e o valor de uma determinada mercadoria de uma loja. Sabendo que o desconto para pagamento à vista é de 10% sobre o valor total,
#    calcular o valor a ser pago à vista. Escrever o nome da mercadoria, o valor total, o valor do desconto e o valor a ser pago à vista.
'''nome = str(input('Nome da mercadoria: '))
valor = float(input('Valor da mercadoria: R$'))
desc = 0.1*valor
total = valor - desc

print('A mercadoria {} possui valor total R${}, com os 10% de desconto (R${}) fica R${} à vista.'.format(nome, valor, desc, total))'''

# Questão 2
# 2. Leia uma cadeia de caracteres no formato “DD/MM/AAAA” e copie o dia, mês e ano para 3 variáveis inteiras. Antes disso, verifique se as barras estão no lugar certo,
#    e se DD, MM e AAAA são numéricos.
'''data = str(input('Informe a data: ')).strip()
dia = data[:2]
mes = data[3:5]
ano = data[6:10]
if data[2]=='/' and data[5]=='/':
    if data[:2].isnumeric() and data[3:5].isnumeric() and data[6:10].isnumeric():
            print('O dia informado é {}.'.format(dia))
            print('O mês informado é {}.'.format(mes))
            print('O ano informado é {}.'.format(ano))
    else:
        print('Os valores informados devem ser numéricos (ex.: 31/12/2030)')
else:
    print('Informe a data no formato correto (DD/MM/AAAA)')'''

# Questão 3
# 3. Escrever um programa que ler do teclado uma string que representa uma cadeia de DNA e gera a cadeia complementar.
# Exemplo: Entrada: AATCTGCAC, Saída: TTAGACGTG.
'''entrada = str(input('Informe a cadeia de DNA: ')).strip().upper()
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
print('O complemento da cadeia {} é {}.'.format(entrada, final))'''

# Questão 4
# 4. Faça um programa que decida se duas strings lidas do teclado são palíndromas mútuas, ou seja, se uma é igual à outra quando lida de traz para frente.
#    Exemplo: amor e roma.
'''P1 = str(input('Digite a palavra 1: ')).strip().lower()
P2 = str(input('Digite a palavra 2: ')).strip().lower()
palavra2 = list(P2)
palavra2.reverse()
palavra2 = "".join(map(str, palavra2))

if P1 == palavra2:
    print('As palavras {} e {} são palíndromas.'.format(P1, P2))
else:
    print('As palavras {} e {} NÃO são palíndromas.'.format(P1, P2))'''

# Questão 5
# 5. Construa um programa que leia duas strings fornecidas pelo usuário e verifique se a segunda string lida esta contida no final da primeira,
#    retornando o resultado da verificação.
pri = str(input('Primeira string: ')).lower().strip()
seg = str(input('Segunda string: ')).lower().strip()

pri = list(pri)
pri.reverse()
seg = list(seg)
seg.reverse()
for k in range(len(seg)):
    if seg[k]==pri[k]:
        resul = 'Está contida.'
    else:
        resul = 'NÃO está contida.'

print(resul)