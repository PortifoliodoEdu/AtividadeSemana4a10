# Algoritmo 70 - Calcular o valor total com a gorjeta em um restaurante

# Solicitar o valor gasto com despesas
cres = float(input("Entre com o valor da conta: "))

# Calcular o valor da gorjeta (10%)
cgorj = cres * 0.1

# Calcular o valor total com a gorjeta
total_com_gorjeta = cres + cgorj

# Imprimir o valor total com a gorjeta formatado com 2 casas decimais
print("\nO valor da conta com a gorjeta será: {:.2f}".format(total_com_gorjeta))
