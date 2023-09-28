import datetime

dist = int(input("Insira a distancia em km: "))
vel = int(input("qual a velocidade média (km/h)"))

print("Tempo de deslocamento (h):", datetime.timedelta(seconds=((dist/vel)*60*60)))

