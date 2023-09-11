# Algoritmo 79 - Cálculo do valor acumulado em uma poupança programada

# Solicitar o valor da aplicação mensal
p = float(input("Digite o valor da aplicação mensal: "))

# Solicitar a taxa (de 0 a 1)
i = float(input("Digite a taxa (0 a 1): "))

# Solicitar o número de meses
n = int(input("Digite o número de meses: "))

# Calcular o valor acumulado
va = p * (((1 + i) ** n) - 1) / i

# Imprimir o valor acumulado
print("\nO valor acumulado na poupança programada é:", va)
