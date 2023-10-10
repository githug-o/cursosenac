notas = []

for i in range(2):
    nota = float(input(f"Insira a nota {i+1}: "))
    notas.append(nota)

soma = 0

for i in range(len(notas)):
    soma = soma + notas[i]

media = soma/2

if media <= 4:
    conceito = "E"
elif 4 < media <= 6:
    conceito = "D"
elif 6 < media <= 7.5:
    conceito = "C"
elif 7.5 < media <= 9:
    conceito = "B"
elif 9 < media:
    conceito = "A"

print("Conceito:", conceito)