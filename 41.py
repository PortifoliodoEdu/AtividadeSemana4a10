# algoritmo 54 - Calcular a média ponderada de quatro números.

# Solicita quatro números ao usuário
a = float(input("Entre com o primeiro número: "))
b = float(input("Entre com o segundo número: "))
c = float(input("Entre com o terceiro número: "))
d = float(input("Entre com o quarto número: "))

# Calcula a média ponderada
mp = (a * 1 + b * 2 + c * 3 + d * 4) / 10

# Imprime a média ponderada
print("Média ponderada:", mp)
