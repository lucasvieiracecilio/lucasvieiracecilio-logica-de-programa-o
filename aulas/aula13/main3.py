class Conta:
    def __init__(self,numero_conta,titular):
        self.numero_conta = numero_conta
        self.titular = titular
        self.saldo  = 0


class ContaCorrente(Conta):
    def __init__(self, numero_conta, titular):
        super().__init__(numero_conta, titular)
        self.cheque_especial = 100
        self.credito = 400

class ContaPoupanca(Conta):
    def __init__(self, numero_conta, titular):
        super().__init__(numero_conta, titular)
        self.
