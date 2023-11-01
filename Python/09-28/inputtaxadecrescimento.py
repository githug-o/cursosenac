hab1 = int(input("insira os habitantes do pais1!: "))
hab2 = int(input("insira os habitantes do pais2!: "))
txpais1 = float(input("insira a taxa de crescimento do pais1!: "))
txpais2 = float(input("insira a taxa de crescimento do pais1!: "))

anos = 0
while hab1<hab2:
    hab1 = hab1*(1+txpais1/100)
    hab2 = hab2*(1+txpais2/100)
    anos = anos+1

print(anos, "anos")