#Calcula a multa sobre o kg excedente do peso do peixe

peso = float(input("Insira o peso do peixe: "))

exc = (peso - 50)
vlrmulta = 4

if peso > 50:
    print("Que peixão em!")
    print("Peso excedente:", exc,"kg")
    print("Multa: R$", exc*vlrmulta)
else:
    print("Que peixinho mixuruca... nem tem multa")