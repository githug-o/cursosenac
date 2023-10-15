from datetime import datetime

livros = []
pessoas = []
emprestimos = []
contatos = []

def cadastro_livro(livros): #teste de input
    print("Insira as informações do livro abaixo:")
    livro={
        'Titulo': input("Título:    "), 
        'Autor': input("Autor:  "),
        'Editora': input("Editora:  ")
    }

    livros.append(livro)
    print("")
    print("------------------")
    print("Livro cadastrado!")
    print("")

def editar_livro(livros):
    ind = int(input("Digite a ID do livro que deseja alterar: "))-1
    if 0 <= ind <= len(livros):
        print("")
        print("Livro escolhido:")
        print(f"ID  |   Título  |   Autor   |   Editora")
        print(f"{ind}  |   {livros[ind]['Titulo']}  |   {livros[ind]['Autor']}   |   {livros[ind]['Editora']}")
        print("")
        livros[ind]['Titulo'] = input("Título: ")
        livros[ind]['Autor'] = input("Autor: ")
        livros[ind]['Editora'] = input("Editora: ")

        print("")
        print("Informações atualizadas")
        print("")
    else:
        print("")
        print("ID de livro não encontrada!")
        print("")

def excluir_livro(livros):
    ind = int(input("Digite a ID do livro que deseja excluir: "))-1
    if 0 <= ind <= len(livros):
        print("")
        print(f"Livro {livros[ind]['Titulo']} excroído!")
        print("")
        del livros[ind]
    else:
        print("")
        print("ID de livro não encontrada!")
        print("")

def imprimir_livros(livros):
    print(f"ID  |   Título  |   Autor   |   Editora ")
    for ind,livros in enumerate(livros):       
        print(f"{ind+1}  |   {livros['Titulo']}  |   {livros['Autor']}   |   {livros['Editora']}")
        
def cadastro_contato(contatos):
    print("")
    print("Insira as informações do contato abaixo:")
    contato={
        'Nome': input("Nome:        "),
        'Telefone': input("Telefone:    "),
        'Email': input("E-mail:     ")
    }
    contatos.append(contato)
    print("Contato salvo!")
    print("")

def editar_contato(contatos):
    ind = int(input("Digite a ID do contato que deseja alterar: "))-1
    if 0 <= ind <= len(contatos):
        print("")
        print("Contato escolhido:")
        print(f"ID  |   Nome  |   Telefone   |   E-mail")
        print(f"{ind}  |   {contatos[ind]['Nome']}  |   {contatos[ind]['Telefone']}   |   {contatos[ind]['Email']}")
        print("")
        livros[ind]['Nome'] = input("Nome:      ")
        livros[ind]['Telefone'] = input("Telefone:  ")
        livros[ind]['Email'] = input("E-mail:       ")

        print("")
        print("Informações atualizadas")
        print("")
    else:
        print("")
        print("ID de contato não encontrada!")
        print("")

def imprimir_contatos(contatos):
    print(f"ID  |   Nome  |   Telefone   |   E-mail ")
    for ind,contatos in enumerate(contatos):       
        print(f"{ind+1}  |   {contatos['Nome']}  |   {contatos['Telefone']}   |   {contatos['Email']}")
        
def excluir_contato(contatos):
    ind = int(input("Digite a ID do contato que deseja excluir: "))-1
    if 0 <= ind <= len(contatos):
        print("")
        print(f"Contato de {contatos[ind]['Nome']} excroído!")
        print("")
        del contatos[ind]
    else:
        print("")
        print("ID de contato não encontrada!")
        print("")

def emprestar(emprestimos,contatos,livros):
    print("Qual livro deseja emprestar?\n")
    imprimir_livros(livros)
    idlivro = int(input("\nDigite a ID do livro: "))-1
    print("")
    print("Para quem?\n")
    imprimir_contatos(contatos)
    idcontato = int(input("\nDigite a ID do contato: "))-1
    print("")
    print("Data do empréstimo:")

    diae = int(input("Digite o dia do empréstimo (dd): "))
    mese = int(input("Digite o mês do empréstimo (mm): "))
    anoe = int(input("Digite o ano do empréstimo (aaaa): "))

    print("")
    print("Data da previsão de devolução:")

    diad = int(input("Digite o dia a previsão de devolução (dd): "))
    mesd = int(input("Digite o mês a previsão de devolução (mm): "))
    anod = int(input("Digite o ano a previsão de devolução (aaaa): "))

        
    emprestimo={
        'Pessoa': contatos[idcontato]['Nome'],
        'Livro': livros[idlivro]['Titulo'],
        'Data': datetime(anoe, mese, diae),
        'Devolucao': datetime(anod, mesd, diad)
    }

    emprestimos.append(emprestimo)

    print("")
    print("Registro de empréstimo realizado com sucesso!")
    print("")

def editar_emprestimo(emprestimos,contatos,livros):
    ind = int(input("Digite a ID do registro de empréstimo que deseja alterar: "))-1
    if 0 <= ind <= len(emprestimos):
        print("")
        print("Registro escolhido:")
        print(f"ID  |   Livro  |   Detentor   |   Dt emprestimo | Dt devolução")
        print(f"{ind+1}  |   {emprestimos[ind]['Livro']}  |   {emprestimos[ind]['Pessoa']}   |   {emprestimos[ind]['Data']}   |   {emprestimos[ind]['Devolucao']}")
        print("")

        print("Qual livro deseja emprestar?\n")
        imprimir_livros(livros)
        idlivro = int(input("\nDigite a ID do livro: "))
        print("")
        print("Para quem?\n")
        imprimir_contatos(contatos)
        idcontato = int(input("\nDigite a ID do contato: "))
        print("")
        print("Data do empréstimo:")

        diae = int(input("Digite o dia do empréstimo (dd): "))
        mese = int(input("Digite o mês do empréstimo (mm): "))
        anoe = int(input("Digite o ano do empréstimo (aaaa): "))

        datae = datetime(anoe, mese, diae)
        print("")
        print("Data da previsão de devolução:")

        diad = int(input("Digite o dia da previsão de devolução (dd): "))
        mesd = int(input("Digite o mês da previsão de devolução (mm): "))
        anod = int(input("Digite o ano da previsão de devolução (aaaa): "))

        datad = datetime(anod, mesd, diad)

        emprestimos[ind]['Pessoa'] = contatos[idcontato]['Nome']
        emprestimos[ind]['Livro'] = livros[idlivro]['Titulo']
        emprestimos[ind]['Data'] = datae
        emprestimos[ind]['Devolucao'] = datad

        print("")
        print("Informações atualizadas")
        print("")
    else:
        print("")
        print("ID de empréstimo não encontrada!")
        print("")

def excluir_registro(emprestimos):
    ind = int(input("Digite a ID do emprestimo que deseja excluir: "))-1
    if 0 <= ind <= len(emprestimos):
        print("")
        print(f"Resgistro de empréstimo do livro {emprestimos[ind]['Livro']} excroído!")
        print("")
        del emprestimos[ind]
    else:
        print("")
        print("ID de emprestimo não encontrada!")
        print("")

def imprimir_emprestimos(emprestimos):
    print(f"ID  |   Status  |   Livro  |   Detentor   |   Dt emprestimo | Dt devolução")
    for ind,contatos in enumerate(emprestimos):

        if emprestimos[ind]['Devolucao'] < datetime.now():
            status = "Atrasado"
        else:
            status = "No prazo"

        print(f"{ind}  |    {status}  |   {emprestimos[ind]['Livro']}  |   {emprestimos[ind]['Pessoa']}   |   {emprestimos[ind]['Data']}")

while True:
    print("Bem-vinde!")
    print("Escolha uma categoria:")
    print("1 - Cadastro de livros")
    print("2 - Cadastro de contatos")
    print("3 - Gestão de empréstimos")
    
    opc1 = int(input(""))
    print("")
    
    if opc1 == 1:
        print("-------------------")
        print("O que deseja fazer:")
        print("1 - Cadastrar um novo livro")
        print("2 - Editar o cadastro de um livro")
        print("3 - Exibir a lista de livros cadastrados")
        print("4 - Excluir um livro dos registros")
        print("")
        opc2 = int(input(""))
        if   opc2 == 1:
            cadastro_livro(livros)
        elif opc2 == 2:
            editar_livro(livros)
        elif opc2 == 3:
            imprimir_livros(livros)
        elif opc2 == 4:
            excluir_livro(livros)
        else:
            print("Opção inválida, tente novamente.")
            print("")

    elif opc1 == 2:
        print("-------------------")
        print("O que deseja fazer:")
        print("1 - Cadastrar um novo contato")
        print("2 - Editar o cadastro de um contato")
        print("3 - Exibir a lista de contatos cadastrados")
        print("4 - Excluir um contato dos registros")
        print("")
        opc2 = int(input(""))
        if   opc2 == 1:
            cadastro_contato(contatos)
        elif opc2 == 2:
            editar_contato(contatos)
        elif opc2 == 3:
            imprimir_contatos(contatos)
        elif opc2 == 4:
            excluir_contato(contatos)
        else:
            print("Opção inválida, tente novamente.")
            print("")

    elif opc1 == 3:
        print("-------------------")
        print("O que deseja fazer:")
        print("1 - Registrar um novo empréstimo")
        print("2 - Editar o registro de um empréstimo")
        print("3 - Exibir a lista de empréstimos")
        print("4 - Excluir um empréstimo dos registros")
        print("")
        opc2 = int(input(""))
        if   opc2 == 1:
            emprestar(emprestimos,contatos,livros)
        elif opc2 == 2:
            editar_emprestimo(emprestimos,contatos,livros)
        elif opc2 == 3:
            imprimir_emprestimos(emprestimos)
        elif opc2 == 4:
            excluir_registro(emprestimos)
        else:
            print("Opção inválida, tente novamente.")
            print("")
