valores = []
for i in range(3):  
    num = float(input(f"Digite o valor do produto {i+1}: "))  
    valores.append(num)
    if menor is None or num < menor:
        menor = num
    else:
        menor = menor
print (valores)
print ("O menor valor é:",menor)