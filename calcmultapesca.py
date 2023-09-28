#Calcula a multa sobre o kg excedente do peso do peixe, se o peso for maior que 50 kg, deve ser pago R$4,00 para cada kg acima dos 50

peso = float(input("Insira o peso do peixe: "))

exc = (peso - 50) #calcula o excedente do peso
vlrmulta = 4 #preço da multa

if peso > 50: #avalia se o peso é maior que 50 kg
    print("Que peixão em!")
    print("Peso excedente:", exc,"kg") #print do peso acima dos 50
    print("Multa: R$", exc*vlrmulta) #print do valor da multa
else:
    print("Que peixinho mixuruca... nem tem multa")
