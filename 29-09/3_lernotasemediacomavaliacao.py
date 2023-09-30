#programa para ler notas no array e calcular a media, mostrar notas e média

notas = [10,5,10,0]
soma = 0

for i in range(len(notas)):
    soma = soma + notas[i]

media = soma/4

if media >=7:
    print("Notas:",notas)
    print("Media:",media)
    print("Approved!")
else:
    print("Notas:",notas)
    print("Media:",media)
    print("Não approved!")

#mesmo do anterior