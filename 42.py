# algoritmo 42 - Calcular funções trigonométricas de um ângulo em graus.

import math

# Solicita um ângulo em graus ao usuário
angulo = float(input("Digite um ângulo em graus: "))
rang = angulo * math.pi / 180

# Calcula e imprime as funções trigonométricas
print("Seno:", math.sin(rang))
print("Co-seno:", math.cos(rang))
print("Tangente:", math.tan(rang))
print("Co-secante:", 1 / math.sin(rang))
print("Secante:", 1 / math.cos(rang))
print("Cotangente:", 1 / math.tan(rang))
