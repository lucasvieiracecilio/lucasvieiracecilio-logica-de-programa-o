

import random
def gerar_senha(tamanho):

   lista_caracteres + ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' ]                       
   
   
   aleatorio = random.choice(lista_caracteres)
   seja_gerada = ""
   for i in range(tamanho):
            seja_gerada += random.choice(lista_caracteres) 
   return seja_gerada
print(gerar_senha(8))
