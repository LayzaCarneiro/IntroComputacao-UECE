# Questão 2
Perguntas = {'P1': ['qual é a sua banda favorita?', 'Los Hermanos!'], 'P2': ['qual é o livro que você mais gostou de ler?', 'O Alquimista - Paulo Coelho.'],
             'P3': ['qual é seu hobby preferido?', 'Ir pra academia.'], 'P4': ['qual é o melhor filme da marvel?', 'Thor Ragnarok.'],
             'P5': ['qual é o melhor esporte que existe?', 'É claro que vôlei!'], 'P6': ['qual é o seu lugar predileto?', 'Praia.'],
             'P7': ['qual é o feriado que você mais gosta?', 'Natal.'], 'P8':['qual é a melhor linguagem de programação?', '!Python'],
             'P9': ['qual é o treino mais legal da semana?', 'Treino de quadríceps.'], 'P10':['qual é o seu doce favorito?', 'Snickers!']}

esc = (input("""Vamos jogar um jogo? Tente adivinhar quais as perguntas são referentes às respostas!
Responda 'Sim' se quiser jogar >>> """)).lower().strip()
pont = 0
iguais = 0
jogador = 0
calc = 0

if esc == 'sim':
    print("""As dez respostas são:
    [1] Los Hermanos!
    [2] O Alquimista - Paulo Coelho.
    [3] Ir pra academia.
    [4] Thor Ragnarok.
    [5] É claro que vôlei!
    [6] Praia.
    [7] Natal.
    [8] !Python
    [9] Treino de quadríceps.
    [10] Snickers!\n""")

    for i in range(len(Perguntas)):
        perg = input('Faça sua pergunta >>  ').lower().strip('?').split()
        if 'qual' in perg:
            for i in Perguntas.keys():
                conferir = (Perguntas[i][0]).strip('?').split()
                if perg == conferir:
                    porcentagem = 100
                    jogador += 1
                    print('Você acertou 100% da pergunta! Um ponto pra você.')
                    break
                else:
                    for k in conferir:
                        if k in perg:
                            iguais += 1
                    porcentagem = (iguais*100)/(len(conferir))
                    if porcentagem > calc:
                        calc = porcentagem
                    iguais = 0
            if perg != conferir and calc >= 60:
                print('Você acertou {:.2f}% da pergunta! Um ponto pra você.'.format(calc))
                pont += 1
            elif perg != conferir and calc < 60:
                print('Você não acertou pelo menos 60% da pergunta. Sem ponto dessa vez.')
            calc = 0
        else:
            print('Eu só aceito perguntas iniciadas por "qual".')

    print('''\nAs perguntas eram:
        [1] qual é a sua banda favorita?
        [2] qual é o livro que você mais gostou de ler?
        [3] qual é seu hobby preferido?
        [4] qual é o melhor filme da Marvel?
        [5] qual é o melhor esporte que existe?
        [6] qual é o seu lugar predileto?
        [7] qual é o feriado que você mais gosta?
        [8] qual é a melhor linguagem de programação?
        [9] qual é o treino mais legal da semana?
        [10] qual é o seu doce favorito?\n''')
    print('PLACAR FINAL: {} com 100% de acerto e {} com pelo menos 60% de acerto.'.format(jogador, pont))

else:
    print("Responda 'Sim' se quiser jogar.")


