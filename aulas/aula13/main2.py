class Animal :
    def __init__(self,nome,cor):
        super().__init__(nome,cor)
        self.nome = nome
        self.cor = cor
class cachorro(Animal):
    def __init__(self,caracteristicas,nome,cor,raça):
        self.caracteristicas = caracteristicas
        self.nome = nome
        self.cor = cor
        self.raça = raça
cachorro1 = cachorro(caracterosticas="parece um rato",nome="paozinho",cor="branco",raça="lulu da pumerania" )
print(vars(cachorro))

class Gato(Animal):
    def __init__(self,Nome,raça,cor):
        self.nome = Nome
        self.raça = raça
        self.cor = cor

cat = Gato (nome = "nina",raça = "branco",cor = "branco")

