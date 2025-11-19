numeros = [-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]



pares = list(filter(lambda x : x % 2 == 0, numeros))
positivos = list(filter(lambda x : x > 0, numeros))
negativos = list(filter(lambda x: x < 0 ,numeros))


print(pares)

print(positivos)

print(negativos)


impares = list(filter(lambda x : x % 2 != 0, numeros))
multiplos_de_3_e_5 = list(filter(lambda x : x % 3==0 and x % 5==0 ,numeros))



print(impares)

print(multiplos_de_3_e_5)

