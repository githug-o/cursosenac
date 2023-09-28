#solicita ao user o salário por hora e a quantidade de horas trabalhadas no mês para calcular salário bruto, descontos e salário líquido
rsporhr = float(input("Insira o salário por hora: "))
hrspormes = int(input("Insira a quantidade de hrs trabalhadas por mês: "))

#bruto, calculado com salário por hora e a quantidade de horas trabalhadas no mês 
salbruto = rsporhr*hrspormes 

#descontos
ir = salbruto*0.11 #11% do salário
inss = salbruto*0.08 #8% do salário
sind = salbruto*0.05 #5% do salário

#líquido
liq = salbruto-inss-sind-ir

print("Salário bruto: R$", salbruto)
print("IR: -R$", ir)
print("INSS: -R$", inss)
print("Sindicato: -R$", sind)
print("Salário líquido: R$", liq)
