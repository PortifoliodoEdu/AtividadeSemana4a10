# Algoritmo 80 - Cálculos da locadora de vídeo

# Solicitar a quantidade de fitas
quant = int(input("Digite a quantidade de fitas: "))

# Solicitar o valor do aluguel por fita
valAluguel = float(input("Digite o valor do aluguel por fita: "))

# Calcular o faturamento anual
fatAnual = quant / 3 * valAluguel * 12

# Calcular o valor das multas mensais
multas = valAluguel * 0.1 * (quant / 3) / 10

# Calcular a quantidade de fitas no final do ano
quantFinal = quant - quant * 0.02 + quant / 10 * 1.08

# Imprimir os resultados
print("\nFaturamento anual da locadora: R$", fatAnual)
print("Valor ganho com multas por mês: R$", multas)
print("Quantidade de fitas no final do ano:", quantFinal)
