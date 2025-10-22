dcionario = []
while True:
    print("="*30)
    print("Cadastro de usuários")
    print("="*30)
    print("1- Cadastrar usuário")
    print("2- telefone Usuário")
    print("3- email Usuário")
    print("4- profissão Usuário")
    print("q - Sair")
    opcao = input("Digite sua opção:")

clites = []
if opcao == "1":
    nome = input("Digite seu nome:")
    clites.append(nome)
    print(f"Usuário {nome} cadastrado com sucesso!")
if opcao == "2":
    telefone = input("Digite seu telefone:")
    clites.append(telefone)
    print(f"Usuário {telefone} cadastrado com sucesso!")
if opcao == "3":
    email = input("Digite seu email:")
    clites.append(email)
    print(f"Usuário {email} cadastrado com sucesso!")
if opcao == "4":
    profissao = input("Digite sua profissão:")
    clites.append(profissao)
    print(f"Usuário {profissao} cadastrado com sucesso!")
    clientes_dicionario.append(clites)
    print(clientes_dicionario)
    if opcao == "q":
      print("Saindo do programa...")
        