# Algoritmo 60 - Calcular o décimo termo de uma PA com base na razão e no primeiro termo

# Solicitar o valor do primeiro termo (a1)
termo = int(input("Digite o valor do 1º termo (a1): "))

# Solicitar a razão da PA (r)
razao = int(input("Digite o valor da razão (r): "))

# Calcular o décimo termo da PA
dec = termo + 9 * razao

# Imprimir o décimo termo
print("\nO 10º termo desta PA é:", dec)
