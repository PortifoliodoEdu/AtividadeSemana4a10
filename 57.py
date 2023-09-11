# Algoritmo 57 - Entrar com as notas da PR1 e PR2 e imprimir a média final

# Solicitar as notas da PR1 e PR2 ao usuário
pr1 = float(input("Digite a nota da PR1: "))
pr2 = float(input("Digite a nota da PR2: "))

# Calcular a média final
media_final = (pr1 + pr2) / 2

# Calcular a média truncada e arredondada
media_truncada = int((media_final - 0.5) + 0.001)
media_arredondada = int(media_final + 0.001)

# Imprimir a média final, média truncada e média arredondada
print("\nMédia final:", media_final)
print("Média truncada:", media_truncada)
print("Média arredondada:", media_arredondada)
