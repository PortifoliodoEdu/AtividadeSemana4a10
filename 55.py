# Algoritmo 55 - Calcular a área de um losango

# Solicitar a medida da diagonal maior e da diagonal menor ao usuário
diagonal_maior = float(input("Medida da diagonal maior: "))
diagonal_menor = float(input("Medida da diagonal menor: "))

# Calcular a área do losango
area = (diagonal_maior * diagonal_menor) / 2

# Imprimir a área do losango
print("Área =", area)
