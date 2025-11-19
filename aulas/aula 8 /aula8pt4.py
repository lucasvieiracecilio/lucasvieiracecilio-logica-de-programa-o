numeros = [1,2,3]
dobro = list(map(lambda x: x * 2, numeros))

numeros = [2,3,4]
sucessor = list(map(lambda x: x + 1, numeros))

numeros = [1,2,3]
antecessor = list(map(lambda x: x - 1, numeros))

numeros = [6,7,8]
sucessor_quintuplo = list(map(lambda x: (x + 1) * 5 , numeros))


print(list(dobro))
print(list(sucessor))
print(list(antecessor))
print(list(sucessor_quintuplo))
