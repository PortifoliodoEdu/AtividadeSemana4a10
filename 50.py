# algoritmo 50 - Calcular o perímetro, a área e a diagonal de um retângulo

import math

# Solicita a base do retângulo ao usuário
base = float(input("Digite a base do retângulo: "))

# Solicita a altura do retângulo ao usuário
altura = float(input("Digite a altura do retângulo: "))

# Calcula o perímetro do retângulo
perimetro = 2 * (base + altura)

# Calcula a área do retângulo
area = base * altura

# Calcula a diagonal do retângulo
diagonal = math.sqrt(base**2 + altura**2)

# Imprime o perímetro, a área e a diagonal do retângulo
print("Perímetro:", perimetro)
print("Área:", area)
print("Diagonal:", diagonal)
