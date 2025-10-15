# Flask 

# LISTAS
# # EStrutura indexada 

# #       0           1      2
# lista = ["GABRIEL","JOAO","ALICE"]

# # método list, encontrar o índice
# print(lista.index("GABRIEL"))

# # ordenando a lista
# lista.sort(reverse=True)

# # verificando se existe este elemento na lista
# print("GABRIEL" in lista)

# #tupla
# # lista é mutável, tupla não

# dados = "ga","ga" # curiosidade
# print(type(dados))

# for dado in dados:
#     print(dado)

# # Dicionários

# cliente = {
#     "nome":'Gabriel'
# }
# cliente = [
#     "Gabriel",
#     "Brasileiro",
#     "autonomo",
#     31,
#     178,
#     2
# ]

clienteD = {
    "nome":"Gabriel",
    "nacionalidade":"Brasileiro",
    "regime_trabalhista":"autonomo",
    "idade":31,
    "saldo":178,
    "qtd_carros":2
}


# for chave in clienteD:
#     print(f"{chave}  {clienteD[chave]}")

# for c,v in clienteD.items():
#     print(f"{c} - {v}")


# SETS

# listas = {"Gabriel","joao","Felipe","Felipe"}
# listas.intersection()
# listas.union()

# # Não guarda posição
# # Não armazena dois valores iguais
# for i in listas:
#     print(i)

