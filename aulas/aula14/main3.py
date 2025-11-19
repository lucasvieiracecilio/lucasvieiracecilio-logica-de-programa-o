class Autor:
    def __init__(self,nome,data_nascimento):
        self.nome = nome 
        self.data_nascimento = data_nascimento


class Livro:
    def __init__(self,titulo,anoPub,autor):
        self.titulo = titulo
        self.anoPub = anoPub
        self.autor = autor

a1 = Autor(nome="CS lewis",data_nascimento="13/05/0001")
t1 = Livro("Como  ser tao pika no clash igual eu",2025,a1)


print(l1.titulo)
print(l1.anoPub)
print(l1.autor.nome)
print(l1.autor.data_nascimento)


