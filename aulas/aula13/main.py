class Carro:
    def __init__(self,modelo_passado,ano_passado,cor_passado):
        #atributos
        self.modelo = modelo_passado
        self.ano = ano_passado
        self.cor = cor_passado
        self.km_rodado = 0
        
    def acelelar(self):
        self.velocidade += 10


modelo = input("digite o modelo do carro:")
carro1 = Carro(modelo_passado="ferrafi"modelo,ano_passado=2025,cor_passado="vermelho")

print(carro1.modelo)
carro1.acelerar
print(carro1.modelo)



