# algoritmo 49 - Imprimir informações sobre um nome

# Solicita um nome ao usuário
nome = input("Entre com um nome: ")

# Imprime o nome completo
print("Todo nome:", nome)

# Imprime o primeiro caractere do nome
print("Primeiro caractere:", nome[0])

# Imprime o último caractere do nome
print("Último caractere:", nome[-1])

# Imprime do primeiro ao terceiro caractere do nome
print("Primeiro ao terceiro caractere:", nome[:3])

# Imprime o quarto caractere do nome
print("Quarto caractere:", nome[3])

# Imprime todos os caracteres do nome, exceto o primeiro
print("Todos menos o primeiro:", nome[1:])

# Imprime os dois últimos caracteres do nome
print("Os dois últimos:", nome[-2:])
