# Algoritmo 81 - Cálculo do dígito verificador da conta corrente

# Solicitar o número da conta corrente com três dígitos
conta = int(input("Digite o número da conta corrente (três dígitos): "))

# Separar os três dígitos da conta
d1 = conta // 100
d2 = (conta % 100) // 10
d3 = conta % 10

# Calcular o número inverso da conta
numero_inverso = d3 * 100 + d2 * 10 + d1

# Somar os dois números
soma = conta + numero_inverso

# Calcular o dígito verificador
digito = (d1 * 1 + d2 * 2 + d3 * 3) % 10

# Imprimir o dígito verificador
print("\nDígito verificador da conta corrente:", digito)
