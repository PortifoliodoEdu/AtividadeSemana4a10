# algoritmo 52 - Calcular o perímetro, a área e a diagonal de um quadrado

import math

# Solicita o lado do quadrado ao usuário
lado = float(input("Digite o lado do quadrado: "))

# Calcula o perímetro do quadrado
perimetro = 4 * lado

# Calcula a área do quadrado
area = lado ** 2

# Calcula a diagonal do quadrado
diagonal = lado * math.sqrt(2)

# Imprime o perímetro, a área e a diagonal do quadrado
print("Perímetro:", perimetro)
print("Área:", area)
print("Diagonal:", diagonal)
