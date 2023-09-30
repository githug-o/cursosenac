numero = [] #define como array e já define como em branco
for i in range(5): #vai repetir 5x
    num = int(input("Digite um número: "))
    numero.append(num) #alimenta o array com o input (5x)
for b in range(len(numero)):
    print(numero[b])

