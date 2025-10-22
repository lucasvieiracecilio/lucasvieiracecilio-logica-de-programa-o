import random

numero_aleatorio = random.randint(1,100)
palpite_jogador = int(input('digite um inteiro de 1 a 100: '))
numero_tentativas = 1
tentativas_passadas = []

while numero_aleatorio != palpite_jogador:

    if palpite_jogador in tentativas_passadas:
        print('já foi, tente outro número')
    else:

        tentativas_passadas.append(palpite_jogador)

        numero_tentativas += 1 # numero_tentativas = numero_tentativas + 1

        if palpite_jogador > numero_aleatorio:
            print('muito alto')
        else:
            print('muito baixo')

    palpite_jogador = int(input('digite um inteiro de 1 a 100: '))


print(f"acertou em {numero_tentativas} tentativas")
print(tentativas_passadas)
