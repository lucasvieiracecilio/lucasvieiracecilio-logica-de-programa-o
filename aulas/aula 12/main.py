# idade = 21
# altura = 1.73
# nome = 'lucas'
# trabalhando = True


# class Pessoa:
#     def __init__(self,nome,alura,idade,peso):
#         self.nome = nome
#         self.altura = altura
#         self.idade = idade 
#         self.peso = peso 

# p1 = Pessoa(nome="lucas",altura =1.87,idade =17,peso =76)

class Dog:
    def __init__(self,nome,raça,idade,peso):
        self.nome = nome
        self.raça = raça
        self.idade = idade
        self.peso = peso
    def __str__(self):
        return f"{self.nome} - {self.raça} - {self.idade} - {self.peso}"


p1 = Dog(nome="paozinho",raça="lulu da pumerania",idade=2,peso=5)

print(vars(p1))
