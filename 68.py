# Algoritmo 68 - Trocar os valores de duas variáveis

# Solicitar o valor de A
a = float(input("Digite o valor de A: "))

# Solicitar o valor de B
b = float(input("Digite o valor de B: "))

# Trocar os valores de A e B usando uma variável auxiliar
aux = a
a = b
b = aux

# Imprimir os valores trocados
print("\nA = ", a)
print("B = ", b)
