# Algoritmo 67 - Cálculo do valor de uma prestação em atraso

# Solicitar o valor da prestação
valor = float(input("Digite o valor da prestação: R$ "))

# Solicitar a taxa de juros em porcentagem
taxa = float(input("Digite a taxa de juros (em %): "))

# Solicitar o tempo em meses
tempo = int(input("Digite o tempo em meses: "))

# Calcular o valor da prestação em atraso
prest = valor + (valor * (taxa / 100) * tempo)

# Imprimir o resultado
print("\nO valor da prestação em atraso é: R$", prest)
