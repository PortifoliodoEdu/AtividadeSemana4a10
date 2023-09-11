# Algoritmo 69 - Converter uma fração em número decimal

# Solicitar o numerador
num = int(input("Digite o numerador: "))

# Solicitar o denominador (certifique-se de evitar a divisão por zero)
denom = int(input("Digite o denominador (não pode ser zero): "))

# Verificar se o denominador é zero
if denom == 0:
    print("Erro: Divisão por zero não permitida.")
else:
    # Calcular o valor decimal da fração
    decimal = num / denom

    # Imprimir o valor decimal
    print("\nDecimal: ", decimal)
