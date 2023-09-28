#O objetivo deste código é calcular o tempo de deslocamento com base na distância e na velocidade média fornecidas pelo usuário e, em seguida, exibir o resultado em horas

import datetime  # Importa a biblioteca datetime para trabalhar com tempo

# Solicita ao usuário que insira a distância em quilômetros e a velocidade média em km/h
dist = int(input("Insira a distancia em km: "))
vel = int(input("Qual a velocidade média (km/h): "))

# Calcula o tempo de deslocamento em segundos usando a fórmula (distância / velocidade) * 60 * 60
tempo_em_segundos = (dist / vel) * 60 * 60

# Converte o tempo de deslocamento de segundos para um objeto timedelta da biblioteca datetime
tempo_deslocamento = datetime.timedelta(seconds=tempo_em_segundos)

# Exibe o tempo de deslocamento em horas
print("Tempo de deslocamento (h):", tempo_deslocamento)

#Esse foi comentado pelo chatGPT
#Este código solicita ao usuário a distância em quilômetros e a velocidade média em quilômetros por hora. Em seguida, ele calcula o tempo de deslocamento usando a fórmula (distância / velocidade) * 60 * 60 para obter o resultado em segundos. Em seguida, converte os segundos em um objeto timedelta da biblioteca datetime e exibe o tempo de deslocamento em horas.
