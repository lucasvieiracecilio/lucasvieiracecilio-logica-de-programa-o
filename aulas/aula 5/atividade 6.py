usuarios = []
while True:
    print("="*30)
    print("Cadastro de usuários")
    print("="*30)
    print("1- Cadastrar usuário")
    print("2- Atualizar Usuário")
    print("3- Deletar Usuário")
    print("4- Listar Usuário")
    print("q - Sair")
    opcao = input("Digite sua opção:")
    
    if opcao == "1":
        nome = input("Digite seu nome:")
        usuarios.append(nome)
        print(f"Usuário {nome} cadastrado com sucesso!")
        
    elif opcao == "2":
      for i, usuario in enumerate(usuarios):
          print(f"{i}: {usuario}")
          indice = int(input("Digite o índice do usuário que deseja atualizar:"))  
      novo_nome = input("Digite o novo nome:")
        
    elif opcao == "3":
        for i, usuario in enumerate(usuarios):
            print(f"{i}: {usuario}")
        indice = int(input("Digite o índice do usuário que deseja deletar:"))  
        usuarios.pop(indice)
        print("Usuário deletado com sucesso!")
    elif opcao == "4":
        for i, usuario in enumerate(usuarios):
            print(f"{i}: {usuario}")
    elif opcao == "q":
        print("Saindo do programa...")
        break
    else:
        print("Resposta Inválida")