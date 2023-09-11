# Algoritmo 66 - Cálculo da quantidade de litros de combustível em uma viagem

# Solicitar o tempo gasto na viagem em horas
tempo = float(input("Digite o tempo gasto na viagem (horas): "))

# Solicitar a velocidade média em km/h
vel = float(input("Digite a velocidade média (km/h): "))

# Calcular a distância percorrida em km
dist = tempo * vel

# Calcular a quantidade de litros de combustível utilizados
litros = dist / 12

# Imprimir os resultados
print("\nVelocidade média:", vel, "km/h")
print("Tempo gasto na viagem:", tempo, "horas")
print("Distância percorrida:", dist, "km")
print("Litros de combustível utilizados:", litros, "litros")
