



import string
import random
def gerar_senha(tamanho):
  letras = string.ascii_letters
  especiais = "!@#$%¨&*()_+{}[];:,.<>/?\|"
  numeros = "0123456789"
  senha_gerada  = ""
  for i in range(tamanho):
    senha_gerada += random.choice(letras + especiais + numeros)
    return senha_gerada
# print(gerar_senha(15))


def descobrirdor_de_senhas(senhas):
    contador = 0
    while True:
            senha_gerada = ""
            for i in range(4):
             senha_gerada += str(random.randint(0,9))
            contador += 1
            print(senha_gerada)
            print(senhas)
            if senha_gerada == senhas:
             print(f"Senha correta {senha_gerada}")
             print(f"Total de tentativas {contador}")
             break      
        # print(random.randint(0,9), end ="")




descobrirdor_de_senhas("1234")