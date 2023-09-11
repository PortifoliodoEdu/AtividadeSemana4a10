# Algoritmo 76 - Sucessor de um número entre 0 e 60

# Solicitar um número entre 0 e 60
num = int(input("Digite um número entre 0 e 60: "))

# Calcular o sucessor, considerando que o sucessor de 60 é 0
sucessor = (num + 1) % 61

# Imprimir o sucessor
print("\nSucessor:", sucessor)
