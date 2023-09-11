# Algoritmo 53 - Calcular a diagonal de um paralelepípedo

import math

# Solicitar os lados a, b e c do paralelepípedo ao usuário
a = float(input("Digite o valor da base: "))
b = float(input("Digite o valor da altura: "))
c = float(input("Digite o valor da profundidade: "))

# Calcular a diagonal do paralelepípedo usando o teorema de Pitágoras
diagonal = math.sqrt(a**2 + b**2 + c**2)

# Imprimir a diagonal do paralelepípedo
print("Diagonal:", diagonal)
