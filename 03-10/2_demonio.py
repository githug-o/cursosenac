def cadastrar_produto(produtos,nome,valor,quantidade,frete,i1,i2,i3,margem,vlrc,vlrv):
    produto = {
        'Nome':nome,
        'Valor':valor,
        'Quantidade':quantidade,
        'Frete':frete,
        'Imp1':i1,
        'Imp2':i2,
        'Imp3':i3,
        'Margem':margem,
        'Valor_custo':vlrc,
        'Valor_venda':vlrv
    }
    produtos.append(produto)
    print(f"")
    print("Produto cadastrado pra carai!")
    print(f"****************************")
    print(f"")

def imprimir_produtos(produtos):
    for indice,produto in enumerate(produtos):
        print(f"****************************")
        print(f"ID do produto:    {indice+1}")
        print(f"Nome:  {produto['Nome']}")
        print(f"Valor:  {produto['Valor']}")
        print(f"Quantidade:  {produto['Quantidade']}")
        print(f"Frete:  {produto['Frete']/produto['Quantidade']}")
        print(f"Imposto 1:  {produto['Valor']*produto['Imp1']}")
        print(f"Imposto 2:  {produto['Valor']*produto['Imp2']}")
        print(f"Imposto 3:  {produto['Valor']*produto['Imp3']}")
        print(f"Margem:  {produto['Valor']*produto['Margem']}")

        custo=produto['Valor']+(produto['Valor']*produto['Imp1'])+(produto['Valor']*produto['Imp2'])+(produto['Valor']*produto['Imp3'])+(produto['Frete']/produto['Quantidade'])

        print(f"Valor de custo:  {custo}")
        print(f"Valor de venda:  {custo+produto['Margem']}")
        print(f"****************************")
        print(f"")

produtos = []
while True:
    opc = int(input(f"Escolha uma opção: \n 1 - Cadastrar produto; \n 2 - Imprimir produtos cadastrados; \n 3 - Sair.\n"))

    if opc == 1:

        nome = input("Digite o nome:    ")
        valor = float(input("Digite o valor:    "))
        quantidade = int(input("Digite a quantidade:    "))
        frete = float(input("Digite o frete:    "))
        i1 = float(input("Digite o imposto 1:   "))/100
        i2 = float(input("Digite o imposto 2:   "))/100
        i3 = float(input("Digite o imposto 3:   "))/100
        margem = float(input("Digite a margem:  "))/100

        vlrc=0
        vlrv=0       

        cadastrar_produto(produtos,nome,valor,quantidade,frete,i1,i2,i3,margem,vlrc,vlrv)
    elif opc == 2:
        imprimir_produtos(produtos)
    else:
        break











