# Questão 2
# 2. Leia uma cadeia de caracteres no formato “DD/MM/AAAA” e copie o dia, mês e ano para 3 variáveis inteiras. Antes disso, verifique se as barras estão no lugar certo,
#    e se DD, MM e AAAA são numéricos.

data = str(input('Informe a data: ')).strip()
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
    print('Informe a data no formato correto (DD/MM/AAAA)')