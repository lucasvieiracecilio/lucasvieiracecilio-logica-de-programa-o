

from random import randint



# Advinhador de Números
# Gere um número aleatório de 1 a 10 (Máquina)
aleatorio = randint(1,10)
print(aleatorio)
# Façam um algoritmo que rode em looping infinito (while True)
while True:
# e receba um número do usuário no intervalo de 1 a 10 (Usuário)
    usuario = int(input("Digite um número no intervalo de 1 a 10:"))
# se  o usuário acertar exiba a mensagem "Parabéns! Você acertou", 
    if aleatorio == usuario:
        print("Parabéns! Você acertou!")
        break 
    elif aleatorio < usuario:
        print("Menos!")
    elif aleatorio > usuario:
        print("Mais!")
    else:
        print("Errou! Tente novamente")
# se o usuário errar exiba a mensagem "Errado! Tente novamente"
# se o número digitado pelo usuário for menor que o número gerado pela máquina, exiba a mensagem "mais". Se for maior, exiba a mensagem "Menos"
# 
