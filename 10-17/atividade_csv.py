import csv #Chamada de biblioteca

produtos = [] #Definindo o Array

def cadastrar_produto(produtos):
    produto = {
        'Nome': input("Digite o nome do produto: "),
        'Valor': float(input("Insira o valor do produto: ")),
        'Quant': int(input("Informe a quantidade:")),
        'Frete': float(input("Insira o valor do frete: ")),
        'Imp1': float(input("Insira o valor do imposto 1: ")),
        'Imp2': float(input("Insira o valor do imposto 2: "))/100,
        'Imp3': float(input("Insira o valor do imposto 3: "))/100,
        'Margem': float(input("Insira a margem de lucro: "))/100,
        'ValorCusto': 0,
        'ValorVenda': 0
    }

    produtos.append(produto)
    criar_csv()
    print("")
    print("Produto cadastrado com sucesso")
    print("")

def criar_csv():
    #with open('arquivo_produtos.csv', mode="w", newline='') as vararquivo COMENTÁRIO DE EXEMPLO
    #writer = csv.writer(vararquivo)
    gravador = csv.writer(open('arquivo_produtos.csv', mode="w", newline='')) 
    gravador.writerow(["Nome","Valor","Quant","Frete","Imp1","Imp2","Imp3","Margem","ValorCusto","ValorVenda"])
    
    for produto in produtos:
            imp1 = produto['Valor']*produto['Imp1']
            imp2 = produto['Valor']*produto['Imp2']
            imp3 = produto['Valor']*produto['Imp3']
            frete = produto['Valor']/produto['Quant']
            vlrcusto = produto['Valor'] + imp1 + imp2 + imp3 + frete              
            margem = vlrcusto * produto['Margem']
            vlrvenda = vlrcusto + margem

            gravador.writerow([produto['Nome'],produto['Valor'],produto['Quant'],frete,imp1,imp2,imp3,margem,vlrcusto,vlrvenda])

def ler_csv():
    with open('arquivo_produtos.csv', mode="r") as vararquivo:
        leitor = csv.DictReader(vararquivo) #linhas como array
        print("Nome","Valor","Quant","Frete","Imp1","Imp2","Imp3","Margem","ValorCusto","ValorVenda")
        for linha in leitor:
            print(f"{linha['Nome']},{linha['Valor']},{linha['Quant']},{linha['Frete']},{linha['Imp1']},{linha['Imp1']},{linha['Imp1']},{linha['Margem']},{linha['ValorCusto']},{linha['ValorVenda']}")            

def exclui_linha(): #rever
    pesquisa = input("Digite o nome que deseja excluir: ")
    for produto in produtos:
        if produto['Nome'] == pesquisa:
            produtos.remove(produto)
        else:
            print("Nome não encontrado na lista!")            
    criar_csv()

def atualizar_dados(produtos):
    pesquisa = input("Digite o nome que deseja atualizar: ")
    for produto in produtos:
        if produto['Nome'] == pesquisa:
            produto['Nome'] = input("Digite o nome do produto: ")
            produto['Valor'] = float(input("Insira o valor do produto: "))
            produto['Quant'] = int(input("Informe a quantidade:"))
            produto['Frete'] = float(input("Insira o valor do frete: "))
            produto['Imp1'] =  float(input("Insira o valor do imposto 1: "))
            produto['Imp2'] =  float(input("Insira o valor do imposto 2: "))/100
            produto['Imp3'] =  float(input("Insira o valor do imposto 3: "))/100
            produto['Margem'] =  float(input("Insira a margem de lucro: "))/100
        else:
            print("Nome não encontrado na lista!")
    
    criar_csv()

while True:
    print("Bem-vinde!")
    print("Escolha um:")
    print("1 - Cadastro")
    print("2 - Ler CSV")
    print("3 - Atualizar informações")
    print("4 - Excluir")
   
    opc = int(input(""))
    print("")
    
    if opc == 1:
        cadastrar_produto(produtos)
    elif opc == 2:
        ler_csv()
    elif opc == 3:
        atualizar_dados(produtos)
    elif opc == 4:
        exclui_linha()

