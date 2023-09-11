# Algoritmo 75 - Cálculo de peso em gramas e novo peso

# Solicitar o peso da pessoa (parte inteira)
peso = int(input("Entre com seu peso, só a parte inteira: "))

# Calcular o peso da pessoa em gramas
pesogramas = peso * 1000

# Calcular o novo peso se a pessoa engordar 12%
novopeso = pesogramas * 1.12

# Imprimir os resultados
print("\nPeso em gramas:", pesogramas)
print("Novo peso:", novopeso)
