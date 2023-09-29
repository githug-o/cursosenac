#programa que leia 5 numeros e informe o maior deles

max = None

for i in range(5):
    num = float(input("digite um número: "))
    if max is None or num > max:
        max = num
    
print("o maior número é", max)

                        