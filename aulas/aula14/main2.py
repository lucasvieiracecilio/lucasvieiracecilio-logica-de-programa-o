from datetime import datetime 
print()
class Conta:
    def __init__(self,saldo,numero,titular):
        self.saldo = saldo
        self.numero = numero
        self.titlar = titular
        self.datetime = datetime.now().date() 

class ContaCorrente(Conta):
    def __init__(self):
        pass