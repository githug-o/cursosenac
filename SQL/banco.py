import mysql.connector

config = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="#0Shippuudens",
    database="mydb"
)

cursor =  config.cursor()

def criar_cliente(nome, email, telefone, tipo,id_endereco):
    sql = "INSERT INTO cliente (nome, email, telefone,tipo, id_endereco) VALUES (%s,%s,%s,%s,%s)"
    val = (nome, email, telefone, tipo,id_endereco)
    cursor.execute(sql, val)
    config.commit()
    print("Cliente inserido com sucesso!")

def listar_clientes():
    cursor.execute("SELECT * FROM cliente")
    clientes = cursor.fetchall()
    for cliente in clientes:
        print(cliente)

def atualizar_cliente(idcliente,nome, email, telefone, tipo,id_endereco):
    sql = "UPDATE cliente SET nome = %s, email = %s, telefone = %s, tipo,id_endereco = %s WHERE idcliente = %s"
    val = (nome, email, telefone, tipo,id_endereco,idcliente)
    cursor.execute(sql, val)
    config.commit()
    print("Cliente atualizado com sucesso!")

def deletar_cliente(idcliente):
    sql = "DELETE FROM cliente WHERE idcliente = %s"
    val = (idcliente,)
    cursor.execute(sql, val)
    config.commit()
    print("Cliente excluído com sucesso!")

while True:
    while True:
        opc = int(input(f"Bem vindo ao sistema ESTOQUE, escolha uma opção: \n" 
                        "1 - Cadastrar cliente\n" 
                        "2 - Imprimir clientes cadastrados\n"
                        "3 - Atualizar info de um cliente\n"
                        "4 - Excluir um cliente\n"
                        "0 - Encerrar\n"))

        if opc == 1:

            nome =      input("Nome:     ")
            email =     input("E-mail:   ")
            telefone =  input("Telefone: ")
            tipo =      input("Tipo:     ")
            id_endereco = int(input("Digite o ID do endereço: "))

            criar_cliente(nome, email, telefone, tipo,id_endereco)
        elif opc == 2:
            listar_clientes()
        elif opc == 3:
            idcliente = input("ID do cliente: ")
            nome =      input("Novo nome:     ")
            email =     input("Novo e-mail:   ")
            telefone =  input("Novo telefone: ")
            tipo =      input("Novo tipo:     ")
            id_endereco = int(input("Digite o novo ID do endereço: "))

            atualizar_cliente(idcliente,nome, email, telefone, tipo,id_endereco)
        elif opc == 4:
            idcliente = input("ID do cliente para ser excluído: ")
            deletar_cliente(idcliente)

        elif opc == 0:
            break
        else:
            print("Insira uma opção válida!")