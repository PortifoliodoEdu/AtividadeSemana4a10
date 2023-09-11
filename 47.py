# algoritmo 47 - Inverter um número no formato CDU

# Solicita um número de 3 dígitos ao usuário
num = int(input("Entre com um número de 3 dígitos: "))

# Separa os dígitos (centenas, dezenas, unidades)
c = num // 100
d = (num % 100) // 10
u = num % 10

# Inverte o número
num_invertido = u * 100 + d * 10 + c

# Imprime o número original e o número invertido
print("Número:", num)
print("Invertido:", num_invertido)
