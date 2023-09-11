# Algoritmo 59 - Calcular a hipotenusa de um triângulo retângulo com base nos catetos

import math

# Solicitar os valores dos catetos ao usuário
b = float(input("Digite o valor do primeiro cateto (b): "))
c = float(input("Digite o valor do segundo cateto (c): "))

# Calcular a hipotenusa
a = math.sqrt(b**2 + c**2)

# Imprimir a hipotenusa
print("\nA hipotenusa é:", a)
