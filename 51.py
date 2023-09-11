# algoritmo 51 - Calcular o perímetro e a área de um círculo

import math

# Solicita o raio do círculo ao usuário
raio = float(input("Digite o raio do círculo: "))

# Calcula o perímetro do círculo
perimetro = 2 * math.pi * raio

# Calcula a área do círculo
area = math.pi * raio ** 2

# Imprime o perímetro e a área do círculo
print("Perímetro:", perimetro)
print("Área:", area)
