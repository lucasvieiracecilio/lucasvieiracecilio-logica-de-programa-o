


# responsabilidade da variável ---> guardar valores
# # responsabilidade da for ---> repetir --> ou iterar
# nome = "Tchimbalanga"
# # round() --> arredonda o valor que esta dentro dele
# print(round(5/2))# pegar somente a parte inteira
# print(5%2)
numeros = [1,2,3,4,5,6,7,8,9,10]
# gerador de intervalor números 
for i in range(1,10,1): 
    print(i)

soma = 0 # variável acumuladora
for i in numeros:
    if i % 2 == 0:
        soma += i
        
# Desafio
# fazer o fatorial de um número
# passo 1 --> receber um NUMERO através do input
# passo2 ---> fazer um contador deste número ate 1 
