
#2. Escreva um programa que lê dia, mês e ano como números e o dia da semana como
# D23456S e escreve por extenso. Por exemplo:
# Entre com o dia >>> 28
# Entre com o mês >>> 9
# Entre com o ano >>> 2022
# Entre com o dia da semana >>> S
# Saída: A data é: : Sábado, 28 de setembro de 2022.

dia = (input('Entre com o dia: '))
mes = (input('Entre com o mês: '))
ano = (input('Entre com o ano: '))
diasem = (input('Entre com o dia da semana: '))
mes_do_ano = {'1':'Janeiro', '2':'Fevereiro', '3':'Março', '4':'Abril', '5':'Maio', '6':'Junho', '7':'Julho', '8':'Agosto', '9':'Setembro', '10':'Outubro', '11':'Novembro', '12':'Dezembro'}
dia_da_semana = {'D': 'Domingo', '2':'Segunda-feira', '3':'Terça-feira', '4':'Quarta-feira', '5':'Quinta-feira', '6':'Sexta-feira','S':'Sábado'}

print('A data é: {}, {} de {} de {}.'.format(dia_da_semana[diasem], dia, mes_do_ano[mes], ano))




