import pyodbc


conexao = pyodbc.connect(
    'DRIVER={SQL Server};SERVER=DESKTOP-CPKGJ7R\SQLEXPRESS;'
    'DATABASE=SOFTWARE')
print('Conexão bem sucedida!')


cursor = conexao.cursor()
comando = "Select * from CADASTRO_PRODUTO"
cursor.execute(comando)
lista = cursor.fetchall()  # Usado para o cursor ler algo no BD

consulta = list(lista)


def consulta_produto(id):
    id = int(id)

    for cod, nome, preco in consulta:
        if id == cod:
            # print(cod, nome, preco)
            # print(type(id))
            return nome, preco
