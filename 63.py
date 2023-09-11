# Algoritmo 63 - Calcular o salário líquido de um professor

# Solicitar o número de aulas dadas no mês
na = int(input("Horas trabalhadas: "))

# Solicitar o valor da hora-aula
vha = float(input("Valor da hora-aula: "))

# Solicitar o percentual de desconto do INSS
pd = float(input("Percentual de desconto do INSS (%): "))

# Calcular o salário bruto
sb = na * vha

# Calcular o valor do desconto do INSS
td = (pd / 100) * sb

# Calcular o salário líquido
sl = sb - td

# Imprimir o salário líquido
print("\nSalário líquido: R$", sl)
