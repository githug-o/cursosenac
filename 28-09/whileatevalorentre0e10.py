while True:
    num = float(input("Insira uma nota entre 0 e 10: "))

    if num >= 0 and num <=10:
        print("Nota valida",num)
        break
    else:
        print("Nota inválida.")