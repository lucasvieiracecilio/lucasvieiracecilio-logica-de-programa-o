clientes = []
from time import sleep
import os
from random import randint

while True:
    print("="*30)
    print("doceria do ze".center(30))
    print("="*30)
    cliente = {}
    cliente["nome"] = input("digite seu nome: ")
    if cliente["nome"] == "sair":
        break
    cliente["telefone"] = input("digite seu telefone: ")
    cliente["email"] = input("digite seu email: ")
    clientes.append(cliente)
    print("\033[31mcliente cadastrado com sucesso!\033[m")
    sleep(5)
    os.system("cls")
    print(clientes)
