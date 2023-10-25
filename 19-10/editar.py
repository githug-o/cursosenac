import csv

def editar_livros():
    leitor = csv.DictReader(open('arquivo_livros.csv', mode="r"))
    editlivro = input("Digite o nome do livro que deseja editar: ")

    for livro in leitor:
        if livro['Titulo'] == editlivro:
            livro['Titulo'] = input("Título: ")
            livro['Editora'] = input("Editora: ")
            livro['Autor'] = input("Autor: ")
        else:
            print("Livro não encontrado.")
    livros = leitor
    criar_livro_csv()

def editar_contatos():
    leitor = csv.DictReader(open('arquivo_livros.csv', mode="r"))
    editcontato = input("Digite o email do contato que deseja editar: ")

    for contato in leitor:
        if contato['Email'] == editcontato:
            contato['Nome'] = input("Nome: ")
            contato['Telefone'] = input("Telefone: ")
            contato['Email'] = input("Email: ")
        else:
            print("Livro não encontrado.")
    contatos = leitor
    criar_contato_csv()

def editar_emprestimos():
    leitor = csv.DictReader(open('arquivo_livros.csv', mode="r"))
    editemprestimo = input("Digite o nome do livro emprestado que deseja alterar: ")
    opc1 = int(input("Qual informação deseja alterar?\n1 - Pessoa;\n2 - Livro;\n3 - Entrega;\n4 - Todas.\n")) 

    for emprestimo in leitor:
        if emprestimo['Livro'] == editemprestimo:
            if opc1 == 1:
                emprestimo['Nome'] = input("Nome: ")
            elif opc1 == 2:
                emprestimo['Livro'] = input("Livro: ") 
            elif opc1 == 3: 
                dia = int(input("Digite o dia a previsão de devolução (dd): "))
                mes = int(input("Digite o mês a previsão de devolução (mm): "))
                ano = int(input("Digite o ano a previsão de devolução (aaaa): "))

                emprestimo['Entrega'] = datetime(ano,mes,dia)
            elif opc1 == 4:             
                emprestimo['Nome'] = input("Nome: ")
                emprestimo['Telefone'] = input("Telefone: ")
                emprestimo['Email'] = datetime(ano,mes,dia)
            else:
                print("Opção inválida!")
        else:
            print("Livro não encontrado.")
    emprestimos = leitor
    criar_emprestimo_csv()


