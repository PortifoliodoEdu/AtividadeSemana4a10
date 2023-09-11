# Algoritmo 72 - Calcular o rendimento de um depósito com base na taxa de juros

# Solicitar o valor do depósito
deposito = float(input("Entre com o valor do depósito: "))

# Solicitar a taxa de juros
taxa = float(input("Entre com a taxa de juros (em porcentagem): "))

# Calcular o valor do rendimento
valor = deposito * taxa / 100

# Calcular o valor total após o rendimento
total = deposito + valor

# Imprimir o valor do rendimento e o valor total
print("\nRendimento: R$ {:.2f}".format(valor))
print("Total após rendimento: R$ {:.2f}".format(total))
