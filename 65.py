# Algoritmo 65 - Calcular o volume de uma lata de óleo

import math

# Solicitar a altura da lata
altura = float(input("Digite a altura da lata: "))

# Solicitar o raio da lata
raio = float(input("Digite o raio da lata: "))

# Calcular o volume da lata usando a fórmula
volume = math.pi * raio**2 * altura

# Imprimir o resultado
print("\nO volume da lata é:", volume)
