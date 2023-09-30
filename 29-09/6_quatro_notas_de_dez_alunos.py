#Programa que pede 4 notas de 5 alunos. Imprimir nome do aluno, as notas, as médias e se esta aprovado ou não

alunos = ["Hugo","Marcus","Isis","Inácio","Luís"]
notas = []
medias = []
soma = 0
cont = 0

for i in range(5):
    for b in range(4):
        nota = float(input(f"Insira a nota de {alunos[i]}: "))
        soma = soma+nota
        media = soma/4
    if media >= 7:
        cont = cont + 1  
    soma = 0
    medias.append(media)

print("média dos alunos", medias)
print("número de alunos com média >= 7:", cont)