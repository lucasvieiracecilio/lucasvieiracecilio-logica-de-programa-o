for i in range (10,0, -1):
    print(i)
fatorial = int(input('qual número deseja o fatorial?'))
resultado = 1
for i in range(fatorial,1,-1):
    resultado *= i
print(f'o fatorial de {fatorial} é {resultado}')