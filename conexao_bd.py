# from sqlite3 import connect
import pyodbc


conexao = pyodbc.connect(
    'DRIVER={SQL Server};SERVER=DESKTOP-CPKGJ7R\SQLEXPRESS;'
    'DATABASE=SOFTWARE')
print('Conexão bem sucedida!')

# cursor = conexao.cursor()
# comando = "insert into CADASTRO_PRODUTO values ('Teste',70,1)"
# cursor.execute(comando)
# cursor.commit()  # Usado para quando o cursor atualiza ou insere algo no BD


class data_base:

    def __init__(self):
        pass

    def cadastrar_produto(self, nome, preco):
        cursor = conexao.cursor()
        comando = f"insert into CADASTRO_PRODUTO values ('{nome}',{preco})"
        cursor.execute(comando)
        cursor.commit()  # Usado para quando o cursor atualiza ou insere algo no BD

    def listar_produtos(self):
        cursor = conexao.cursor()
        comando = "select * from CADASTRO_PRODUTO"
        cursor.execute(comando)
        lista = cursor.fetchall()  # Usado para o cursor ler algo no BD
        return lista

    def atualizar_produtos(self, dado):
        cursor = conexao.cursor()
        comando = f"""update CADASTRO_PRODUTO set 
                    PRODUTO = '{dado[1]}',
                    PRECO = '{dado[2]}'
                    where IDPRODUTO = '{dado[0]}' """
        cursor.execute(comando)
        cursor.commit()  # Usado para atualizar algo no BD

    def deletar_produtos(self, id):
        cursor = conexao.cursor()
        comando = f"""delete from CADASTRO_PRODUTO 
                    where idproduto = '{id}' """
        cursor.execute(comando)
        cursor.commit()  # Usado para deletar algo no BD

    def venda(self):
        cursor = conexao.cursor()
        comando = "select * from CADASTRO_PRODUTO"
        cursor.execute(comando)
        lista_venda = cursor.fetchall()  # Usado para o cursor ler algo no BD
        return lista_venda

    def listar_venda_produto(self):
        cursor = conexao.cursor()
        comando = "select * from VENDA"  # order by ID_LANCAMENTO
        cursor.execute(comando)
        lista = cursor.fetchall()  # Usado para o cursor ler algo no BD
        return lista

    def venda_produto(self, id, nome, preco, qtd, preco_total, lancamento):
        cursor = conexao.cursor()
        comando_venda = f"insert into VENDA values ({id},'{nome}',{preco},{qtd},{preco_total},{lancamento})"
        cursor.execute(comando_venda)
        cursor.commit()

    def registro_lancamento(self, id_lancamento, valor_venda, f_pg):
        cursor = conexao.cursor()
        comando = f"insert into LANCAMENTO values ({id_lancamento},{valor_venda},'{f_pg}')"
        cursor.execute(comando)
        cursor.commit()

# CADASTRAR PRODUTO
# db_cadastro = data_base()
# db_cadastro.cadastrar_produto('Garrafa', 30)


# SELECIONAR TABELA
# db_listar = data_base()
# db_listar.listar_produtos()


# ATUALIZAR ITEM DA TABELA
# db_atualiza = data_base()
# db_atualiza.atualizar_produtos()


# DELETAR ITEM DA TABELA
# db_delete = data_base()
# db_delete.deletar_produtos()

# # CADASTRAR VENDA
# db_venda = data_base()
# db_venda.venda_produto(26, 'Pizza G (Carne do Sol)', 50, 2, 100, 1)

# SELECIONAR TABELA LANCAMENTO
# db_lancamento = data_base()
# db_lancamento.lancamento()

# SELECIONAR TABELA
# db_lista_venda = data_base()
# db_lista_venda.venda()

# CADASTRAR LANCAMENTO
# db_venda_lancamento = data_base()
# db_venda_lancamento.registro_lancamento(2, 100, 'cartão')
