# Algoritmo 78 - Cálculo do número de diagonais de um polígono convexo

# Solicitar o número de lados do polígono
n = int(input("Digite o número de lados do polígono: "))

# Calcular o número de diagonais diferentes (nd)
nd = n * (n - 3) / 2

# Imprimir o número de diagonais
print("\nNúmero de diagonais do polígono:", nd)
