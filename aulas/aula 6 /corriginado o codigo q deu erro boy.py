clientes = []
cliente = {}
for i in range(3):
    cliente["nome"] = input("Digite o nome do cliente: ")
    cliente["telefone"] = input("Digite o telefone do cliente: ")
    cliente["email"] = input("Digite o email do cliente: ")
    cliente["profissao"] = input("Digite a profissão do cliente: ")
    clientes.append(cliente.copy())
for cliente in clientes:
    print(cliente)
