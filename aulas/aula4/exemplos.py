notas_e_moedas = [200, 100, 50, 20, 10, 5, 2, 1, 0.50, 0.25, 0.05, 0.01]

# valor e receber : 1700 reais

# valor recebido: 2000 reais


valor_a_receber = float(input('qual valor a receber'))
qual_valor_recebido = float(input('qual valor recebido'))
#  1700
# 2000


diferença = qual_valor_recebido - valor_a_receber
# 300
for item in notas_e_moedas: # 200
    quantidad_de_itens = 0 
    while item <= diferença: # 200 < 300
         quantidad_de_itens += 1
         diferença -= item
         if quantidad_de_itens > 0:
             print(f'{quantidad_de_itens} itens de valor {item}')

# Print(diferença)


