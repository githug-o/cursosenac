#Este código tem como objetivo calcular a velocidade média com base na distância e no tempo de deslocamento em minutos fornecidos pelo usuário e, em seguida, exibir o resultado em quilômetros por hora (km/h).

import datetime  # Importa a biblioteca datetime para uso futuro (não é usada neste código)

# Solicita ao usuário que insira a distância em quilômetros e o tempo de deslocamento em minutos
dist = float(input("Insira a distancia em km: "))
t = float(input("Tempo de deslocamento em minutos: "))

# Calcula a velocidade média dividindo a distância pela quantidade de tempo em horas (t/60)
velocidade_media = dist / (t / 60)

# Exibe a velocidade média em km/h
print("Velocidade média:", velocidade_media, "km/h")

#Neste código, o usuário insere a distância em quilômetros e o tempo de deslocamento em minutos. Em seguida, ele calcula a velocidade média dividindo a distância pela quantidade de tempo em horas (t/60) para converter o tempo de minutos para horas. O resultado é a velocidade média em km/h, que é então exibida na tela.

