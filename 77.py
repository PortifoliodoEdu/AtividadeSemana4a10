# Algoritmo 77 - Quadrado da diferença e diferença dos quadrados

# Solicitar dois números reais
a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))

# Calcular o quadrado da diferença
diferenca_quadrado = (a - b) ** 2

# Calcular a diferença dos quadrados
diferenca_quadrados = a ** 2 - b ** 2

# Imprimir os resultados
print("\nO quadrado da diferença é:", diferenca_quadrado)
print("A diferença dos quadrados é:", diferenca_quadrados)
