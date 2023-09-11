# Algoritmo 71 - Calcular quantos minutos se passaram desde o início do dia

# Solicitar a hora atual
hora = int(input("Entre com a hora atual: "))

# Solicitar os minutos atuais
minuto = int(input("Entre com os minutos atuais: "))

# Calcular o total de minutos desde o início do dia
tminuto = hora * 60 + minuto

# Imprimir a quantidade de minutos passados
print("\nAté agora se passaram: {} minutos".format(tminuto))
