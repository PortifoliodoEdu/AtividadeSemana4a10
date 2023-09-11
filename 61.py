# Algoritmo 61 - Calcular o quinto termo de uma PG com base na razão e no primeiro termo

# Solicitar o valor do primeiro termo (a1)
termo = int(input("Digite o valor do 1º termo (a1): "))

# Solicitar a razão da PG (q)
razao = int(input("Digite o valor da razão (q): "))

# Calcular o quinto termo da PG
quinto = termo * (razao ** 4)

# Imprimir o quinto termo
print("\nO 5º termo desta PG é:", quinto)
