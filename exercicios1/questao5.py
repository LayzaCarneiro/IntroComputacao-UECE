print('1) Decimal para binário. ')
print('2) Decimal para octal. ')
print('3) Decimal para hexadecimal. ')
print('4) Binário para decimal. ')
print('5) Binário para octal. ')
print('6) Binário para hexadecimal. ')
print('7) Octal para decimal. ')
print('8) Octal para binário. ')
print('9) Octal para hexadecimal. ')
print('10) Hexadecimal para decimal. ')
print('11) Hexadecimal para binário. ')
print('12) Hexadecimal para octal. ')
print(' ')
esc = int(input('Escolha uma das opções acima: '))

if esc == 1:
    num = int(input('Insira o número em decimal: '))
    dec = num
    Lbin = []
    while num > 0:
        resto = num%2
        binario = resto
        num = num//2
        Lbin.insert(0, binario)
    resul = "".join(map(str, Lbin))
    print('O número decimal {} em binário é: {}'.format(dec, resul))

elif esc == 2:
    num = int(input('Insira o número em decimal: '))
    dec = num
    Lo = []
    while num > 0:
        resto = num%8
        octal = resto
        num = num//8
        Lo.insert(0, octal)
    resul = "".join(map(str, Lo))
    print('O número decimal {} em octal é: {}'.format(dec, resul))

elif esc == 3:
    num = int(input('Insira o número em decimal: '))
    dec = num
    Lh = []
    while num > 0:
        resto = num%16
        hexa = resto
        num = num//16
        if hexa==10:
            hexa = 'A'
        elif hexa==11:
            hexa = 'B'
        elif hexa==12:
            hexa = 'C'
        elif hexa==13:
            hexa = 'D'
        elif hexa==14:
            hexa = 'E'
        elif hexa==15:
            hexa = 'F'
        Lh.insert(0, hexa)
    resul = "".join(map(str, Lh))
    print('O número decimal {} em hexadecimal é: {}'.format(dec, resul))

elif esc == 4:
    bin = (input('Insira o número em binário:'))
    d = 0
    for b in range(len(bin)):
        d = d + int(bin[b]) * 2 ** (len(bin) - 1 - b)
    print('O número binário {} em decimal é: {}'.format(bin, d))

elif esc == 5:
    bin = str(input('Insira o número em binário: '))
    Lb = []
    L = []
    i = len(bin) - 1
    octal = 0
    while i >= 0:
        Lb.append(int(bin[i]))
        i -= 1
    for i, k in enumerate(Lb):
        octal += (2**i)*k
    while octal > 1:
        b = int(octal%8)
        octal = octal/8
        L.insert(0, b)
        resul = "".join(map(str, L))
    print('O número binário {} em octal é: {}'.format(bin, resul))

elif esc == 6:
    bin = str(input('Insira o número em binário: '))
    Lb = []
    L = []
    i = len(bin) - 1
    hexa = 0
    while i >= 0:
        Lb.append(int(bin[i]))
        i -= 1
    for i, k in enumerate(Lb):
        hexa += (2**i)*k
    while hexa > 1:
        b = int(hexa%16)
        if (b == 10):
            b = 'A'
        elif (b == 11):
            b = 'B'
        elif (b == 12):
            b = 'C'
        elif (b == 13):
            b = 'D'
        elif (b == 14):
            b = 'E'
        elif (b == 15):
            b = 'F'
        hexa = hexa/16
        L.insert(0, b)
        resul = "".join(map(str, L))
    print('O número bínario {} em hexadecimal é: {}'.format(bin, resul))

elif esc == 7:
    octal = (input('Insira o número em octal:'))
    d = 0
    for b in range(len(octal)):
        d = d + int(octal[b]) * 8 ** (len(octal) - 1 - b)
    print('O número octal {} em decimal é: {}'.format(octal, d))

elif esc == 8:
    octal = str(input('Insira o número em octal: '))
    Lo = []
    L = []
    i = len(octal) - 1
    bin = 0
    while i >= 0:
        Lo.append(int(octal[i]))
        i -= 1
    for i, k in enumerate(Lo):
        bin += (8**i)*k
    while bin > 1:
        b = int(bin%2)
        bin = bin/2
        L.insert(0, b)
        resul = "".join(map(str, L))
    print('O número octal {} em binário é: {}'.format(octal, resul))

elif esc == 9:
    octal = (input('Insira o número em octal:'))
    d = 0
    for b in range(len(octal)):
        d = d + int(octal[b]) * 8 ** (len(octal) - 1 - b)

    Lh = []
    while d > 0:
        resto = d % 16
        hexa = resto
        d = d // 16
        if hexa == 10:
            hexa = 'A'
        elif hexa == 11:
            hexa = 'B'
        elif hexa == 12:
            hexa = 'C'
        elif hexa == 13:
            hexa = 'D'
        elif hexa == 14:
            hexa = 'E'
        elif hexa == 15:
            hexa = 'F'
        Lh.insert(0, hexa)
    resul = "".join(map(str, Lh))
    print('O número octal {} em hexadecimal é: {}'.format(octal, resul))

elif esc == 10:
    hexa = (input('Insira o número em hexadecimal:')).upper()
    num = hexa
    hexa = list(hexa)
    d = 0
    for b in range(len(hexa)):
        if hexa[b] == "A":
            hexa[b] = 10
        elif hexa[b] == "B":
            hexa[b] = 11
        elif hexa[b] == "C":
            hexa[b] = 12
        elif hexa[b] == "D":
            hexa[b] = 13
        elif hexa[b] == "E":
            hexa[b] = 14
        elif hexa[b] == "F":
            hexa[b] = 15
        d = d + int(hexa[b]) * 16 ** (len(hexa) - 1 - b)
    print('O número hexadecimal {} em decimal é: {}'.format(num, d))

elif esc == 11:
    hexa = str(input("Insira o número em hexadecimal:  ")).upper()
    L = [ESC for ESC in hexa]
    L1 = []
    n = len(L) - 1
    bin = 0
    for i in range(len(L)):
        if L[i] == "A":
            L[i] = 10
        elif L[i] == "B":
            L[i] = 11
        elif L[i] == "C":
            L[i] = 12
        elif L[i] == "D":
            L[i] = 13
        elif L[i] == "E":
            L[i] = 14
        elif L[i] == "F":
            L[i] = 15
        else:
            L[i] = int(L[i])
        add = L[i]*(16**n)
        bin += add
        n -= 1
    while bin > 1:
        b = int(bin%2)
        bin = bin / 2
        L1.insert(0, b)
        resul = "".join(map(str, L1))
    print('O número hexadecimal {} em binário é: {}'.format(hexa, resul))

elif esc == 12:
    hexa = (input('Insira o número em hexadecimal:')).upper()
    num = hexa
    hexa = list(hexa)
    d = 0
    for b in range(len(hexa)):
        if hexa[b] == "A":
            hexa[b] = 10
        elif hexa[b] == "B":
            hexa[b] = 11
        elif hexa[b] == "C":
            hexa[b] = 12
        elif hexa[b] == "D":
            hexa[b] = 13
        elif hexa[b] == "E":
            hexa[b] = 14
        elif hexa[b] == "F":
            hexa[b] = 15
        d = d + int(hexa[b]) * 16 ** (len(hexa) - 1 - b)

    Lo = []
    while d > 0:
        resto = d % 8
        octal = resto
        d = d // 8
        Lo.insert(0, octal)
    resul = "".join(map(str, Lo))
    print('O número hexadecimal {} em octal é: {}'.format(num, resul))

