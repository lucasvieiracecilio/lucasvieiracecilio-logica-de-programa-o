from datetime import datetime 
print()

clientes = {}
produtos = {}
vendas = {}

def cadastrar_cliente():
    nome = input("Nome do cliente: ").strip()
    if nome in clientes:
        print("Cliente já existe.")
        return
    clientes[nome] = {"compras": 0}
    print("Cliente cadastrado.")



def cadastrar_produto():
    nome = input("Nome do produto: ").strip()
    if nome in produtos:
        print("Produto já existe.")
        return
    try:
        preco = float(input("Preço: "))
        estoque = int(input("Quantidade em estoque: "))
    except ValueError:
        print("Valores inválidos.")
        return
    produtos[nome] = {"preco": preco, "estoque": estoque}
    print("Produto cadastrado.")



def vender_produto():
    cliente = input("Cliente: ").strip()
    if cliente not in clientes:
        print("Cliente não encontrado.")
        return

    produto = input("Produto: ").strip()
    if produto not in produtos:
        print("Produto não encontrado.")
        return

    try:
        qtd = int(input("Quantidade: "))
    except ValueError:
        print("Quantidade inválida.")
        return

    if produtos[produto]["estoque"] < qtd:
        print("Estoque insuficiente.")
        return

    total = produtos[produto]["preco"] * qtd
    produtos[produto]["estoque"] -= qtd
    clientes[cliente]["compras"] += total
    vendas.append({"cliente": cliente, "produto": produto, "qtd": qtd, "total": total})

    print(f"Venda registrada. Total: R$ {total:.2f}")

def gerar_estatisticas():
    print("\n=== Estatísticas ===")
    total_vendas = sum(v["total"] for v in vendas)
    print(f"Total vendido: R$ {total_vendas:.2f}")

    if vendas:
        produto_mais_vendido = max(produtos, key=lambda p: produtos[p]["estoque"])
        print(f"Produto com maior estoque restante: {produto_mais_vendido}")
    else:
        print("Nenhuma venda realizada ainda.")

    if clientes:
        top_cliente = max(clientes, key=lambda c: clientes[c]["compras"])
        print(f"Cliente que mais gastou: {top_cliente} (R$ {clientes[top_cliente]['compras']:.2f})")
    else:
        print("Nenhum cliente cadastrado.")

    print("====================\n")


while True:
    print("""
==== MENU ====
1 - Cadastrar Cliente
2 - Cadastrar Produto
3 - Vender Produto
4 - Gerar Estatísticas
0 - Sair
""")
    op = input("Escolha: ")

    if op == "1":
        cadastrar_cliente()
    elif op == "2":
        cadastrar_produto()
    elif op == "3":
        vender_produto()
    elif op == "4":
        gerar_estatisticas()
    elif op == "0":
        print("Encerrado.")
        break
    else:
        print("Opção inválida.")