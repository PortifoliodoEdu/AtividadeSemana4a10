# algoritmo 44 - Calcular o logaritmo de um número em uma base específica.

import math

# Solicita um número ao usuário
num = float(input("Entre com o logaritmando: "))

# Solicita a base ao usuário (certifique-se de inserir uma base diferente de 1)
base = float(input("Entre com a base (diferente de 1): "))

# Verifica se a base é diferente de 1 para evitar a divisão por zero
if base != 1:
    # Calcula o logaritmo na base especificada
    logaritmo = math.log(num) / math.log(base)
    
    # Imprime o logaritmo
    print(f"Logaritmo de {num} na base {base} é igual a {logaritmo}")
else:
    print("A base deve ser diferente de 1 para calcular o logaritmo corretamente.")
