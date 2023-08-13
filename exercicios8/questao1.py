# Questão 1
Perguntas = {'P1': ['qual é a sua banda favorita?', 'Los Hermanos!'], 'P2': ['qual é o livro que você mais gostou de ler?', 'O Alquimista - Paulo Coelho.'],
             'P3': ['qual é seu hobby preferido?', 'Ir pra academia!'], 'P4': ['qual é o seu maior medo?', 'Estar vivendo errado.'], 'P5': ['qual é o melhor filme da Marvel?', 'Thor Ragnarok.'],
             'P6': ['qual é o melhor esporte que existe?', 'É claro que vôlei!'], 'P7': ['qual é o seu objetivo de vida?', 'Ser mochileira e viver viajando.'],
             'P8': ['qual é o seu lugar predileto?', 'Praia.'], 'P9': ['qual é o feriado que você mais gosta?', 'Natal.'], 'P10':['qual é a melhor linguagem de programação?', '!Python'],
             'P11': ['qual é o treino mais legal da semana?', 'Treino de quadríceps.'], 'P12':['qual é o seu doce favorito?', 'Snickers!']}

perg = input('Faça sua pergunta >>  ').lower().strip('?').split()
iguais = 0
pont = 0
resposta = " "

if 'qual' in perg:
    for i in Perguntas.keys():
        conferir = (Perguntas[i][0]).strip('?').split()
        if perg == conferir:
            print('Resposta: ', Perguntas[i][1])
        else:
            for k in conferir:
                if k in perg:
                    iguais += 1
            if iguais < 3:
                iguais = 0
            if iguais >= 3:
                if iguais > pont:
                    pont = iguais
                    resposta = Perguntas[i][1]
                iguais = 0
    print('Resposta: ', resposta)

elif perg == []:
    print('Fim.')
elif 'qual' not in perg:
    print('Eu só sei responder algumas perguntas são iniciadas por "qual".')
else:
    print("Não entendi, refaça a sua pergunta.")
