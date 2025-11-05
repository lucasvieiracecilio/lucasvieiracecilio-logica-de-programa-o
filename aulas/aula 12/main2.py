from time import sleep
import os 
class Carro:
    def __init__(self,modelo,ano,cor):
        self.modelo= modelo
        self.ano = ano
        self.cor= cor
        self.velocidade_do_carro = 0
    def acelerar(self):
        self.velocidade_do_carro = int(input("digite a velocidade")) 
        return self.velocidade_do_carro

    def __str__(self):
        return f"{self.modelo} - {self.ano} - {self.cor} - {self.velocidade_do_carro}" 
# print(carro.velocidade_do_carro)
carros = []
while True:
    print("="*50)
    print("bem vindo a concecionaria qual carro deseja?")
    print("="*50)
    print("1- cadrastras carro")
    print("2- listar carros")
    # print("2- cor")
    # print("3- velocidade do carro")
    
    opcao = input("Digite sua opção:")
    if opcao == "1":
        modelo = input("digite seu modelo:")
        ano = input("digite o ano:")
        cor = input("digite a cor:")
        carro = Carro(modelo,ano,cor)
        carros.append(carro)
        print(f"este carro {modelo} esta cadrastrado")
    elif opcao == "2":
       
       for car in carros:
           print(f"{car.modelo} - {car.ano}")
    sleep(5)
    os.system("clear")
    # elif opcao == "3":
    #    velocidade_do_carro= input("digite sua velocidade max:")
    #    carro.append(velocidade_do_carro)
    #    print(f"esta velocidade maxima:{velocidade_do_carro} esta cadrastrada")
