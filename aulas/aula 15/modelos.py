class Cliente:
    def __init__(self,nome = None,telefone = None, gasto = None ):
        self.nome = nome
        self.telefone = telefone
        self.gasto_total = gasto

   

    def cadastrar_cliente(self):
        nomes = input("Digite seu nome")
        telefones = input("Digite seu telefone")
        gasto = input("Digite seus gastos")
        

        return Cliente(nomes, telefones, gasto)





class Produtos:
    def __init__(self,nome,quantidade,preço_unitario):
        self.nome = nome
        self.quantidade = quantidade
        self.preço_unitario = preço_unitario
        self.total_produto_estoque = self.quantidade * self.preço_unitario

    
class estoque:
    def __init__(self):
        self.clientes = []
        self.produtos = []

        
    def cadastrar_produto(self,produto,produtos,nome):
        self.produto.append(produto)
        print("produto cadrastrado com sucesso")
        if nome in produtos:
         print("Produto já existe.")
         return
   
   
    print("Produto cadastrado.")
    def vender_produto(self):
         pass

    

class preço_unitario(self):
 c = Cliente()   # só pra conseguir chamar o método
pessoa = c.cadastrar_cliente()
print(pessoa.nome, pessoa.telefone, pessoa.gasto_total)

class estatistica:
