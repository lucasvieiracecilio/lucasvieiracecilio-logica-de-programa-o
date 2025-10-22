import random

numero_aleatorio = random.randint(1,10)
palpite_jogador = int(input('digite um inteiro de 1 a 10: '))
numero_tentativas = 1
tentativas_passadas = []

while True: 
    numero_aleatorio != palpite_jogador

    if palpite_jogador in tentativas_passadas:
        print('errado tente novamente')
    else:

        tentativas_passadas.append(palpite_jogador)

        numero_tentativas += 1 # numero_tentativas = numero_tentativas + 1

        if palpite_jogador > numero_aleatorio:
            print('menos')
        else:
            print('mais')

        palpite_jogador = int(input('digite um inteiro de 1 a 10: '))


    print(f"acertou em {numero_tentativas} tentativas") 
    print(tentativas_passadas)
    break