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