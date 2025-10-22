# Limite da variável --> somente guarda uma informação por vez
#            0        1         2      3   
clientes = ["Larica","Gabriel","Anna","Zé"] # definindo uma lista vazia

# função do print()--> exibir no terminal

# Imprimir no terminal o cliente da posição 0,1,2,3
# print(clientes[0])
# print(clientes[1])
# print(clientes[2])
# print(clientes[3])
# Imprimir no terminal o úlitmo cliente
# print(clientes[-1])# ultimo elemento

# percorre uma lista 
# qualquer estrutura que pode ser percorrida

# for cliente in clientes:
#     print(cliente)


# para adicionar novos elementos no final da lista
# clientes.append("Novo nome")

# Para remover elementos pelo conteúdo 

# clientes.remove("Gabriell")

# Para remover pelo índice pop()
# print(clientes)
# clientes.pop()
print(clientes)
clientes[2] = "novo"
print(clientes)