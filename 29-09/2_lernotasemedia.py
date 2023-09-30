#programa para ler notas no array e calcular a media, mostrar notas e média

notas = [10,5,10,0] #definição do array
soma = 0 #definição de 0 para o primeiro valor de soma, precisa estar aqui para a variável estar definida antes de usar num calculo

#for para repetir a soma
#enquanto 'i' (o local do array) estiver dentro do 'len(notas)'
#len dá o tamanho do array, nesse caso, o valor que aparece ali é 3 (0, 1, 2, 3), então a soma vai ser realizada 4 vezes
for i in range(len(notas)): 
    soma = soma + notas[i] #aqui a cara repetição vai ser adicionado a variavel soma a soma de cada nota com a da casa anterior

print("Notas:",notas) #fora do FOR, imprime a array lá de cima
print("Média:", soma/4) # aqui pega a soma de todos no FOR e divide por 4