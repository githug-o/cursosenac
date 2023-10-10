valores = []
for i in range(3):
    
    num = float(input(f"Digite o nome do produto {i+1}: "))
    valores.append(num)

print (valores)
print ("O menor valor é:",min(valores))

