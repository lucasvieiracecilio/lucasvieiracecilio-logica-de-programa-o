
while True:
    print("="*30)
    print("escolha a operação que deseja realizar")
    print("="*30)
    print("1- soma")
    print("2- subtracao")
    print("3- multiplicacao")
    print("4- dividisao")
    print("q - Sair")
    opcao = input("Digite sua opção:")
    n1 = int(input("Digite o primeiro número: "))
    n2 = int(input("Digite o segundo número: "))
    if opcao == "1":
     def somar(n1, n2):




       resultado = n1 + n2
       return resultado


    print(somar(n1,n2))
    if opcao == "2":
      def subtrair(n1, n2):
       resultado = n1 - n2
       return resultado
    print(subtrair(n1,n2))
    if opcao == "3":
      def multiplicar (n1, n2):
       resultado = n1 * n2
       return resultado
    print(multiplicar(n1,n2))
    if opcao == "4":
      def dividir (n1, n2):
       resultado = n1 / n2
       return resultado
    print(dividir(n1,n2))
    if opcao == "q":
      print("Saindo do programa...")
      break

        
