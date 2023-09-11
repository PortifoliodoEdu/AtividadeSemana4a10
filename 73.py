# Algoritmo 73 - Manipulação de números reais

# Solicitar um número real
num = float(input("Entre com um número real com parte fracionária: "))

# Calcular a parte inteira do número
numi = int(num)

# Calcular a parte fracionária do número
numfrac = num - numi

# Arredondar o número
numa = round(num)

# Imprimir os resultados
print("\nParte inteira:", numi)
print("Parte fracionária:", "{:.3f}".format(numfrac))
print("Número arredondado:", numa)
