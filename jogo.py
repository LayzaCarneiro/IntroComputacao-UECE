#Layza Carneiro - Pedra, Papel ou Tesoura
nome = input(' Digite seu nome/apelido:  ').title().strip()
print(f'\033[1;32m {nome}, vamos jogar pedra, papel ou tesoura? \033[m')
vezes = int(input(f' Quantas partidas você quer jogar, {nome}?  '))
partida = 1
computador = ['Pedra', 'Tesoura', 'Pedra', 'Papel', 'Tesoura', 'Papel', 'Tesoura', 'Pedra', 'Papel', 'Tesoura', 'Papel',
              'Tesoura', 'Pedra', 'Pedra', 'Papel', 'Tesoura', 'Pedra', 'Papel', 'Tesoura', 'Pedra', 'Papel', 'Tesoura', 'Pedra',
              'Pedra','Papel', 'Tesoura', 'Pedra', 'Papel', 'Pedra', 'Papel', 'Tesoura', 'Pedra', 'Papel', 'Papel',
              'Pedra', 'Tesoura', 'Papel', 'Tesoura', 'Tesoura', 'Pedra', 'Papel', 'Tesoura', 'Pedra', 'Papel',
              'Tesoura', 'Pedra', 'Tesoura', 'Papel', 'Papel', 'Tesoura', 'Pedra']
pont_comp = 0
pont_jogador = 0

while vezes > 0:
    print('\n',f'\033[1;32mPARTIDA {partida}\033[m')
    numero = int(input(' Primeiro escolha um número aleatório entre 0 e 50:  '))
    print('-=-'*20, '\n Agora escolha um número entre as opções abaixo: \n [1] Pedra\n','[2] Papel\n','[3] Tesoura ')
    jogador = int(input(' Escolha:  '))
    print('-=-'*20)

    if (jogador < 1 or jogador > 3 ) or (numero < 0 or numero > 50): print('\033[4;32m Escolha inválida. Lembre que tem que inserir o valor dentro da faixa pedida.\033[m')
    else:
        if jogador == 1: jogador = 'Pedra'
        elif jogador == 2: jogador = 'Papel'
        elif jogador == 3: jogador = 'Tesoura'

        escolha = computador.pop(numero)
        computador.append(jogador)

        if escolha == jogador:
            pont_jogador +=  1
            pont_comp += 1
            print(f'\033[1;33m Empatamos!! Eu também escolhi {jogador}.\033[m \n', f'Pontuação:\n {nome}: {pont_jogador}\n Computador: {pont_comp}')
        elif (escolha == 'Pedra' and jogador == 'Papel') or (escolha == 'Papel' and jogador == 'Tesoura') or (escolha == 'Tesoura' and jogador == 'Pedra'):
            pont_jogador += 1
            print(f'\033[1;34m Parabéns, você ganhou essa partida!! Eu tinha escolhido {escolha}.\033[m \n', f'Pontuação:\n {nome}: {pont_jogador}\n Computador: {pont_comp} ')
        else:
            pont_comp += 1
            print('\033[1;31m Dessa vez você perdeu, um ponto pra mim! :)\n', f'Você escolheu {jogador} e eu escolhi {escolha}!\033[m \n', f'Pontuação:\n {nome}: {pont_jogador}\n Computador: {pont_comp} ')
        vezes -= 1
        partida += 1

if pont_jogador == pont_comp:
    print(f'\n \033[1;33mEMPATAMOS!!\n {nome}, foi muito legal jogar com você. A pontuação final ficou:\033[m \n {nome}: {pont_jogador}\n Computador: {pont_comp}')
elif pont_jogador > pont_comp:
    print(f'\n \033[1;34mVOCÊ GANHOU!!\n {nome}, foi muito legal jogar com você. A pontuação final ficou:\033[m \n {nome}: {pont_jogador}\n Computador: {pont_comp}')
else:
    print(f'\n \033[1;31mVOCÊ PERDEU ;)\n {nome}, foi muito legal jogar com você. A pontuação final ficou:\033[m \n {nome}: {pont_jogador}\n Computador: {pont_comp}')
