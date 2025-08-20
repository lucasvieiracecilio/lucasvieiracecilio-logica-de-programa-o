import random

print("Bem-vindo ao jogo de adivinhação!")
print("tente adivinhar o número entre 1 e 100.")

numero_secreto = random.randint(1, 100)
palpite_jogador = int(input("Digite seu palpite: "))

while palpite_jogador != numero_secreto: