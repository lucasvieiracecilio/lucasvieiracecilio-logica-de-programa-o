class Cliente:
    def __init__(self, nome=None, telefone=None, gasto_total=0):
        self.nome = nome
        self.telefone = telefone
        self.gasto_total = gasto_total

    def cadastrar_cliente(self):
        nome = input("Digite seu nome: ")
        telefone = input("Digite seu telefone: ")
        return Cliente(nome, telefone, 0)


class Produto:
    def __init__(self, nome, quantidade, preco_unitario):
        self.nome = nome
        self.quantidade = quantidade
        self.preco_unitario = preco_unitario
        self.vendas = 0
        self.faturamento = 0

    def vender(self, qtd):
        if qtd > self.quantidade:
            print("Estoque insuficiente.")
            return False

        self.quantidade -= qtd
        self.vendas += qtd
        self.faturamento += qtd * self.preco_unitario
        return True


class Estoque:
    def __init__(self):
        self.clientes = []
        self.produtos = []
        self.total_vendas = 0

    def cadastrar_produto(self, nome, quantidade, preco_unitario):
        for p in self.produtos:
            if p.nome == nome:
                print("Produto já existe.")
                return
        novo = Produto(nome, quantidade, preco_unitario)
        self.produtos.append(novo)
        print("Produto cadastrado.")

    def cadastrar_cliente(self):
        c = Cliente()
        cliente = c.cadastrar_cliente()
        self.clientes.append(cliente)
        print("Cliente cadastrado.")
        return cliente

    def vender_produto(self, nome_produto, nome_cliente, quantidade):
        # localiza produto
        produto = next((p for p in self.produtos if p.nome == nome_produto), None)
        if not produto:
            print("Produto não encontrado.")
            return

        # localiza cliente
        cliente = next((c for c in self.clientes if c.nome == nome_cliente), None)
        if not cliente:
            print("Cliente não encontrado.")
            return

        if produto.vender(quantidade):
            valor = quantidade * produto.preco_unitario
            cliente.gasto_total += valor
            self.total_vendas += valor
            print(f"Venda concluída. Total: R$ {valor}")

    def gerar_estatisticas(self):
        print("\n===== ESTATÍSTICAS DO ESTOQUE =====")

        print(f"\n→ Total de vendas do estoque: R$ {self.total_vendas}")

        print("\n→ Total gasto por cliente:")
        for c in self.clientes:
            print(f"   {c.nome}: R$ {c.gasto_total}")

        print("\n→ Faturamento por produto:")
        for p in self.produtos:
            print(f"   {p.nome}: R$ {p.faturamento}")

        # mais vendido
        mais_vendido = max(self.produtos, key=lambda p: p.vendas, default=None)
        menos_vendido = min(self.produtos, key=lambda p: p.vendas, default=None)

        if mais_vendido:
            print(f"\n→ Produto mais vendido: {mais_vendido.nome} ({mais_vendido.vendas} vendas)")
        if menos_vendido:
            print(f"→ Produto menos vendido: {menos_vendido.nome} ({menos_vendido.vendas} vendas)")

        print("====================================\n")


# Exemplo de uso manual
e = Estoque()

