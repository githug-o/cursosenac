#
vt = [] 
vti = []
vtp = []

for i in range(10):
    num = int(input("Digite um número: "))
    vt.append(num)
    if vt[i]%2 == 0:
        vtp.append(num)
    else:
        vti.append(num)
print("Vetor:",vt)
print("Vetor par:",vti)
print("Vetor par:",vtp)