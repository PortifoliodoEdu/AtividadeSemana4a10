# Algoritmo 58 - Calcular o valor de x com base em xnum1, xnum2 e xnum3

import math

# Solicitar os valores de xnum1, xnum2 e xnum3 ao usuário
xnum1 = float(input("Digite o primeiro valor (xnum1): "))
xnum2 = float(input("Digite o segundo valor (xnum2): "))
xnum3 = float(input("Digite o terceiro valor (xnum3): "))

# Calcular o valor de x
x = xnum1 + xnum2 / (xnum3 + xnum1) + 2 * (xnum1 - xnum2) + math.log(64) / math.log(2)

# Imprimir o valor de x
print("\nValor de x:", x)
