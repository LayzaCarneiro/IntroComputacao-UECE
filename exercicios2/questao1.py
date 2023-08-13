# Questão 1
# 1. Ler o nome e o valor de uma determinada mercadoria de uma loja. Sabendo que o desconto para pagamento à vista é de 10% sobre o valor total,
#    calcular o valor a ser pago à vista. Escrever o nome da mercadoria, o valor total, o valor do desconto e o valor a ser pago à vista.

nome = str(input('Nome da mercadoria: '))
valor = float(input('Valor da mercadoria: R$'))
desc = 0.1*valor
total = valor - desc

print('A mercadoria {} possui valor total R${}, com os 10% de desconto (R${}) fica R${} à vista.'.format(nome, valor, desc, total))