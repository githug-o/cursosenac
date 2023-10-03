nomes_produtos = []
valores_produtos = []
quantidades = []
valor_frete =[]

taxa_imposto1 = []
taxa_imposto2 = []
taxa_imposto3 = []

margem = []

custos_individuais = []

while False:
    opc = int(input(f"Escolha uma opção: \n 1 - Cadastrar produto; \n 2 - Imprimir produtos cadastrados; \n 3 - Sair.\n"))

    if opc >= 1 and opc <= 3:
        break
    else:
        print("Digite um número válido!")

    if opc == 3:
        print("Xau!")
        
    elif opc == 1:
        opc2 = 1
        while opc2 == 1:
            novo_produto = input("Nome do produto: ")
            novo_vlr_produto = float(input("Valor do produto: "))
            novo_qtd = int(input("Quantidade: "))
            novo_frete = float(input("Frete: "))

            novo_tx_imp1 = float(input("Valor de imposto 1: "))/100
            novo_tx_imp2 = float(input("Valor de imposto 2: "))/100
            novo_tx_imp3 = float(input("Valor de imposto 3: "))/100

            nova_margem = float(input("Margem de lucro: "))/100

            nomes_produtos.append(novo_produto)
            valores_produtos.append(novo_vlr_produto)
            quantidades.append(novo_qtd)
            valor_frete.append(novo_frete)

            taxa_imposto1.append(novo_tx_imp1)
            taxa_imposto2.append(novo_tx_imp2)
            taxa_imposto3.append(novo_tx_imp3)

            margem.append(nova_margem)

            opc2 = int(input(f"Escolha uma opção: \n 1 - Cadastrar produto; \n 2 - Imprimir produtos cadastrados; \n 3 - Sair.\n"))
        if opc2 == 2:
            
            print(f"Produto | Valor | Frete | Qtd | Imp1 | Imp2 | Imp3 | Margem | Custo i | Venda i")
            for i in range(len(nomes_produtos)):

                frete = valor_frete[i]/quantidades[i]
                i1 = valores_produtos[i]*taxa_imposto1[i]
                i2 = valores_produtos[i]*taxa_imposto2[i]
                i3 = valores_produtos[i]*taxa_imposto3[i]

                vlrc = valores_produtos[i]+i1+i2+i3+frete

                print(f"{nomes_produtos[i]} | {valores_produtos[i]:.2f} | {frete:.2f} | {quantidades[i]} | {i1:.2f} | {i2:.2f} | {i3:.2f} | {margem[i]*100:.1f}% |{vlrc:.2f} | {vlrc*(1+margem[i]):.2f}")

