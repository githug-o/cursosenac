rsporhr = float(input("Insira o salário por hora: "))
hrspormes = int(input("Insira a quantidade de hrs trabalhadas por mês: "))

salbruto = rsporhr*hrspormes
ir = salbruto*0.11
inss = salbruto*0.08
sind = salbruto*0.05
liq = salbruto-inss-sind-ir

print("Salário bruto: R$", salbruto)
print("IR: -R$", ir)
print("INSS: -R$", inss)
print("Sindicato: -R$", sind)
print("Salário líquido: R$", liq)