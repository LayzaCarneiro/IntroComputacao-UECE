# Questão 5

valores = {'Valor1': 1, 'Valor2': 2, 'Valor3': 3, 'Valor4': 4, 'Valor5': 5}
maior1 = max(valores.values())
maior2 = 0
L = []

for i in valores.items():
    L.append(i)
for i in valores.values():
    if i > maior2 and i < maior1:
        maior2 = i
for k,v in enumerate(valores.values()):
    if v == maior1:
        pos1 = k
for k, v in enumerate(valores.values()):
    if v == maior2:
        pos2 = k

print(f'O par chave-valor do maior elemento do dicionário é {L[pos1]}.')
print(f'E o par chave-valor do segundo maior elemento do dicionário é {L[pos2]}.')