from datetime import datetime 
print()

class Conta:
    def __init__(self,numero_conta,titular):# Método construtor
        self.numero_conta = numero_conta
        self.titular = titular 
        self.saldo = 0
        self.data_criacao = datetime.now().date() 

class ContaCorrente(Conta):
    def __init__(self, numero_conta, titular):
        super().__init__(numero_conta, titular)
        self.cheque_especial = 400
    
    def sacar(self,valor_saque):
        # retirar o valor do saldo
        self.saldo -= valor_saque
        pass
    
    def depositar(self,valor_deposito):
        # adicionar o valor no saldo
        pass

    def transferir(self,conta_destinada:Conta):
        # decrementa de uma conta e adiciona na outra 
        pass

class ContaPoupanca(Conta):
    def __init__(self, numero_conta, titular):
        super().__init__(numero_conta, titular)
    
    def gerar_juros(self):
        # gera um juros de 1% sobre o saldo
        pass 


conta1 = ContaCorrente("010203","Joao Pescador")
print(conta1.saldo)
conta1.sacar(10)
print(conta1.saldo)


