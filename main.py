from ast import Return
import sys
from turtle import width
from unittest import result
from webbrowser import Elinks
from tela_vendas import *
from conexao_bd import *
from PyQt5.QtWidgets import QMainWindow, QTableView, QWidget, QApplication, QPushButton, QTableWidget, QTableWidgetItem, QMessageBox
import pandas as pd
from consulta import consulta_produto


class Vendas(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

# TOGGLE BUTTON #############################################################

        self.btn_toggle.clicked.connect(self.LeftContainer)


# CONFIGURAÇÃO DOS BOTÕES LATERAIS PARA ACESSO AS PAGINAS #####################

        self.btn_home.clicked.connect(
            lambda: self.Pages.setCurrentWidget(self.pg_home))

        self.btn_cadastro.clicked.connect(
            lambda: self.Pages.setCurrentWidget(self.pg_cadastro))

        self.btn_teladevendas.clicked.connect(
            lambda: self.Pages.setCurrentWidget(self.pg_venda))

# CONFIGURAÇÃO DOS BOTÕES DAS PAGINAS #########################################

        self.btn_cadastro_produto.clicked.connect(self.cadastro_produto)

        self.btn_atualizar.clicked.connect(self.lista)

        self.btn_alterar.clicked.connect(self.atualiza)

        self.btn_excluir.clicked.connect(self.excluir)

        self.btn_excel.clicked.connect(self.gerar_excel)

        self.lista()
################################# TELA DE VENDAS ##############################

        # Linha 01
        self.txt_cod_1.editingFinished.connect(self.consultar)
        self.txt_qtd_1.editingFinished.connect(self.consultar)

        # Linha 02
        self.txt_cod_2.editingFinished.connect(self.consultar)
        self.txt_qtd_2.editingFinished.connect(self.consultar)

        # Linha 03
        self.txt_cod_3.editingFinished.connect(self.consultar)
        self.txt_qtd_3.editingFinished.connect(self.consultar)

        # Linha 04
        self.txt_cod_4.editingFinished.connect(self.consultar)
        self.txt_qtd_4.editingFinished.connect(self.consultar)

        # Linha 05
        self.txt_cod_5.editingFinished.connect(self.consultar)
        self.txt_qtd_5.editingFinished.connect(self.consultar)

        # Linha 06
        self.txt_cod_6.editingFinished.connect(self.consultar)
        self.txt_qtd_6.editingFinished.connect(self.consultar)

        # Linha 07
        self.txt_cod_7.editingFinished.connect(self.consultar)
        self.txt_qtd_7.editingFinished.connect(self.consultar)

        # self.lineEdit_forma_pg_2.editingFinished.connect(self.consultar)
        self.lineEdit_valor_pago_2.editingFinished.connect(self.consultar)

        self.btn_finalizar_venda.clicked.connect(self.cadastro_venda)


# CONFIGURAÇÃO DO MENU ESQUERDO PARA ACESSO AOS BOTOES DAS PAGINAS ###########

    def LeftContainer(self):
        width = self.left_container.width()

        if width == 9:
            new_width = 200
        else:
            new_width = 9

        self.animation = QtCore.QPropertyAnimation(
            self.left_container, b"maximumWidth")
        self.animation.setDuration(500)
        self.animation.setStartValue(width)
        self.animation.setEndValue(new_width)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()

# CONFIGURAÇÃO DAS TELAS #####################################################

    def cadastro_produto(self):
        db = data_base()
        conectar = conexao
        print(conectar)

        dados = (self.txt_nomeproduto.text(), self.txt_preco.text())
        self.txt_nomeproduto.clear()
        self.txt_preco.clear()
        db.cadastrar_produto(dados[0], dados[1])

        self.lista()

    def lista(self):
        db = data_base()
        conectar = conexao
        print(conectar)
        result = db.listar_produtos()
        # print(result)

        self.tb_produtos.clearContents()
        self.tb_produtos.setRowCount(len(result))

        for row, text in enumerate(result):
            for column, data in enumerate(text):
                self.tb_produtos.setItem(
                    row, column, QTableWidgetItem(str(data)))

    def atualiza(self):
        dados = []
        lista_atualizada = []

        for row in range(self.tb_produtos.rowCount()):
            for column in range(self.tb_produtos.columnCount()):
                dados.append(self.tb_produtos.item(row, column).text())
            lista_atualizada.append(dados)
            dados = []

        db = data_base()
        conectar = conexao
        print(conectar)

        db.atualizar_produtos(tuple(lista_atualizada))

        self.tb_produtos.reset()
        self.lista()

    def excluir(self):
        db = data_base()
        conectar = conexao
        print(conectar)

        produto = self.tb_produtos.selectionModel().currentIndex().siblingAtColumn(0).data()
        db.deletar_produtos(produto)
        self.lista()
        # print(delete)

    def gerar_excel(self):
        dados = []
        todos_dados = []

        for row in range(self.tb_produtos.rowCount()):
            for column in range(self.tb_produtos.columnCount()):
                dados.append(self.tb_produtos.item(row, column).text())

            todos_dados.append(dados)
            dados = []

        columns = ['IDPRODUTO', 'PRODUTO', 'PRECO']

        produtos = pd.DataFrame(todos_dados, columns=columns)
        produtos.to_excel(
            "Produtos Teste.xlsx", sheet_name='Lista de produtos', index=False)

#### TELA DE VENDAS ###########################################################

    def consultar(self):
        db = data_base()
        conectar = conexao
        print(conectar)
        result1 = db.listar_produtos()

        valor_pago = self.lineEdit_valor_pago_2.text()

        # LINHA 1
        id = self.txt_cod_1.text()
        qtd = self.txt_qtd_1.text()

        # LINHA 2
        id2 = self.txt_cod_2.text()
        qtd2 = self.txt_qtd_2.text()

        # LINHA 3
        id3 = self.txt_cod_3.text()
        qtd3 = self.txt_qtd_3.text()

        # LINHA 4
        id4 = self.txt_cod_4.text()
        qtd4 = self.txt_qtd_4.text()

        # LINHA 5
        id5 = self.txt_cod_5.text()
        qtd5 = self.txt_qtd_5.text()

        # LINHA 6
        id6 = self.txt_cod_6.text()
        qtd6 = self.txt_qtd_6.text()

        # LINHA 7
        id7 = self.txt_cod_7.text()
        qtd7 = self.txt_qtd_7.text()

        #--------------------------------------------------------------------#

        # CONFIGURAÇÃO LINHA 01

        for cod, nome, preco in result1:
            if id == '':
                self.txt_cod_1.setText(str(0))
                print('Comparando se ID está em branco')
                return

            elif int(id) == cod:  # int(id) == cod
                print('Verificando se ID contem na lista de produtos')
                print(f'elif tem o tipo {type(id)}')
                self.txt_produto_1.setText(str(nome))
                self.txt_preco_1.setText(str(f'R$ {preco:.2f}'))

                if qtd == '':
                    self.txt_qtd_1.setText(str(0))
                    print('Comparando se QTD está em branco')

                elif qtd != '':
                    print('Verificando se QTD é diferente de em branco')
                    preco_total = int(qtd) * float(preco)
                    self.txt_produto_1.setText(str(nome))
                    self.txt_preco_1.setText(str(f'R$ {preco:.2f}'))
                    self.txt_precototal_1.setText(str(f'R$ {preco_total:.2f}'))

                    # SOMA
                    soma_itens = preco_total + 0

                    self.lineEdit_valor_total_2.setText(
                        str(f'R$ {soma_itens:.2f}'))

                    if valor_pago == '':
                        self.lineEdit_valor_pago_2.setText(str(''))
                    elif valor_pago != '':
                        valor_pago_int = float(valor_pago)
                        self.lineEdit_valor_pago_2.setText(
                            str(f'R$ {valor_pago_int:.2f}'))

                        troco = valor_pago_int - float(soma_itens)
                        self.lineEdit_troco_2.setText(str(f'R$ {troco:.2f}'))

        # CONFIGURAÇÃO LINHA 02

        for codigo2, item2, valor2 in result1:
            if id2 == '':
                self.txt_cod_2.setText(str(''))
                print('Comparando se ID está em branco')
                return

            elif int(id2) == codigo2:
                print('Verificando se ID contem na lista de produtos')
                print(f'elif tem o tipo {type(id2)}')
                self.txt_produto_2.setText(str(item2))
                self.txt_preco_2.setText(str(f'R$ {valor2:.2f}'))

                if qtd2 == '':
                    self.txt_qtd_2.setText(str(0))
                    print('Comparando se QTD está em branco')

                elif qtd2 != '':
                    print('Verificando se QTD é diferente de em branco')
                    preco_total2 = int(qtd2) * float(valor2)
                    self.txt_produto_2.setText(str(item2))
                    self.txt_preco_2.setText(str(f'R$ {valor2:.2f}'))
                    self.txt_precototal_2.setText(
                        str(f'R$ {preco_total2:.2f}'))

                    # SOMA2

                    # soma_itens = total1 + total2
                    soma_itens = preco_total + preco_total2

                    self.lineEdit_valor_total_2.setText(
                        str(f'R$ {soma_itens:.2f}'))

                    if valor_pago == '':
                        self.lineEdit_valor_pago_2.setText(str(''))
                    elif valor_pago != '':
                        valor_pago_int = float(valor_pago)
                        self.lineEdit_valor_pago_2.setText(
                            str(f'R$ {valor_pago_int:.2f}'))

                        troco = valor_pago_int - float(soma_itens)
                        self.lineEdit_troco_2.setText(str(f'R$ {troco:.2f}'))

        # CONFIGURAÇÃO LINHA 03

        for codigo3, item3, valor3 in result1:
            if id3 == '':
                self.txt_cod_3.setText(str(''))
                return

            elif int(id3) == codigo3:
                self.txt_produto_3.setText(str(item3))
                self.txt_preco_3.setText(str(f'R$ {valor3:.2f}'))

                if qtd3 == '':
                    self.txt_qtd_3.setText(str(0))

                elif qtd3 != '':
                    preco_total3 = int(qtd3) * float(valor3)
                    self.txt_produto_3.setText(str(item3))
                    self.txt_preco_3.setText(str(f'R$ {valor3:.2f}'))
                    self.txt_precototal_3.setText(
                        str(f'R$ {preco_total3:.2f}'))

                    # SOMA3

                    # soma_itens = total1 + total2
                    soma_itens = preco_total + preco_total2 + preco_total3

                    self.lineEdit_valor_total_2.setText(
                        str(f'R$ {soma_itens:.2f}'))

                    if valor_pago == '':
                        self.lineEdit_valor_pago_2.setText(str(''))
                    elif valor_pago != '':
                        valor_pago_int = float(valor_pago)
                        self.lineEdit_valor_pago_2.setText(
                            str(f'R$ {valor_pago_int:.2f}'))

                        troco = valor_pago_int - float(soma_itens)
                        self.lineEdit_troco_2.setText(str(f'R$ {troco:.2f}'))

        # CONFIGURAÇÃO LINHA 04

        for codigo4, item4, valor4 in result1:
            if id4 == '':
                self.txt_cod_4.setText(str(''))
                return

            elif int(id4) == codigo4:
                self.txt_produto_4.setText(str(item4))
                self.txt_preco_4.setText(str(f'R$ {valor4:.2f}'))

                if qtd4 == '':
                    self.txt_qtd_4.setText(str(0))

                elif qtd4 != '':
                    preco_total4 = int(qtd4) * float(valor4)
                    self.txt_produto_4.setText(str(item4))
                    self.txt_preco_4.setText(str(f'R$ {valor4:.2f}'))
                    self.txt_precototal_4.setText(
                        str(f'R$ {preco_total4:.2f}'))

                    # SOMA4

                    soma_itens = preco_total + preco_total2 + preco_total3 + preco_total4

                    self.lineEdit_valor_total_2.setText(
                        str(f'R$ {soma_itens:.2f}'))

                    if valor_pago == '':
                        self.lineEdit_valor_pago_2.setText(str(''))
                    elif valor_pago != '':
                        valor_pago_int = float(valor_pago)
                        self.lineEdit_valor_pago_2.setText(
                            str(f'R$ {valor_pago_int:.2f}'))

                        troco = valor_pago_int - float(soma_itens)
                        self.lineEdit_troco_2.setText(str(f'R$ {troco:.2f}'))

        # CONFIGURAÇÃO LINHA 05

        for codigo5, item5, valor5 in result1:
            if id5 == '':
                self.txt_cod_5.setText(str(''))
                return

            elif int(id5) == codigo5:
                self.txt_produto_5.setText(str(item5))
                self.txt_preco_5.setText(str(f'R$ {valor5:.2f}'))

                if qtd5 == '':
                    self.txt_qtd_5.setText(str(0))

                elif qtd5 != '':
                    preco_total5 = int(qtd5) * float(valor5)
                    self.txt_produto_5.setText(str(item5))
                    self.txt_preco_5.setText(str(f'R$ {valor5:.2f}'))
                    self.txt_precototal_5.setText(
                        str(f'R$ {preco_total5:.2f}'))

                    # SOMA5

                    soma_itens = preco_total + preco_total2 + \
                        preco_total3 + preco_total4 + preco_total5

                    self.lineEdit_valor_total_2.setText(
                        str(f'R$ {soma_itens:.2f}'))

                    if valor_pago == '':
                        self.lineEdit_valor_pago_2.setText(str(''))
                    elif valor_pago != '':
                        valor_pago_int = float(valor_pago)
                        self.lineEdit_valor_pago_2.setText(
                            str(f'R$ {valor_pago_int:.2f}'))

                        troco = valor_pago_int - float(soma_itens)
                        self.lineEdit_troco_2.setText(str(f'R$ {troco:.2f}'))

        # CONFIGURAÇÃO LINHA 06

        for codigo6, item6, valor6 in result1:
            if id6 == '':
                self.txt_cod_6.setText(str(''))
                return

            elif int(id6) == codigo6:
                self.txt_produto_6.setText(str(item6))
                self.txt_preco_6.setText(str(f'R$ {valor6:.2f}'))

                if qtd6 == '':
                    self.txt_qtd_6.setText(str(0))

                elif qtd6 != '':
                    preco_total6 = int(qtd6) * float(valor6)
                    self.txt_produto_6.setText(str(item6))
                    self.txt_preco_6.setText(str(f'R$ {valor6:.2f}'))
                    self.txt_precototal_6.setText(
                        str(f'R$ {preco_total6:.2f}'))

                    # SOMA6
                    soma_itens = preco_total + preco_total2 + preco_total3 + \
                        preco_total4 + preco_total5 + preco_total6

                    self.lineEdit_valor_total_2.setText(
                        str(f'R$ {soma_itens:.2f}'))

                    if valor_pago == '':
                        self.lineEdit_valor_pago_2.setText(str(''))
                    elif valor_pago != '':
                        valor_pago_int = float(valor_pago)
                        self.lineEdit_valor_pago_2.setText(
                            str(f'R$ {valor_pago_int:.2f}'))

                        troco = valor_pago_int - float(soma_itens)
                        self.lineEdit_troco_2.setText(str(f'R$ {troco:.2f}'))

        # CONFIGURAÇÃO LINHA 07

        for codigo7, item7, valor7 in result1:
            if id7 == '':
                self.txt_cod_7.setText(str(''))
                return

            elif int(id7) == codigo7:
                self.txt_produto_7.setText(str(item7))
                self.txt_preco_7.setText(str(f'R$ {valor7:.2f}'))

                if qtd7 == '':
                    self.txt_qtd_7.setText(str(0))

                elif qtd7 != '':
                    preco_total7 = int(qtd7) * float(valor7)
                    self.txt_produto_7.setText(str(item7))
                    self.txt_preco_7.setText(str(f'R$ {valor7:.2f}'))
                    self.txt_precototal_7.setText(
                        str(f'R$ {preco_total7:.2f}'))

                    # SOMA7

                    soma_itens = preco_total + preco_total2 + preco_total3 + \
                        preco_total4 + preco_total5 + preco_total6 + preco_total7

                    self.lineEdit_valor_total_2.setText(
                        str(f'R$ {soma_itens:.2f}'))

                    if valor_pago == '':
                        self.lineEdit_valor_pago_2.setText(str(''))
                    elif valor_pago != '':
                        valor_pago_int = float(valor_pago)
                        self.lineEdit_valor_pago_2.setText(
                            str(f'R$ {valor_pago_int:.2f}'))

                        troco = valor_pago_int - float(soma_itens)
                        self.lineEdit_troco_2.setText(str(f'R$ {troco:.2f}'))

###############################################################################

###############################################################################

    def cadastro_venda(self):
        db = data_base()
        conectar = conexao
        print(conectar)
        lancamento_id = db.listar_venda_produto()

        f_pg = self.lineEdit_forma_pg_2.text()
        dados_lancamento = []

        for cod, nome, preco, quantidade, preco_total, lancamento in lancamento_id:
            dados_lancamento.append(lancamento)
        print('Dados Lançamento:')
        print(max(dados_lancamento, key=int) + 1)

        dados_linha1 = (self.txt_cod_1.text(), self.txt_produto_1.text(),
                        self.txt_preco_1.text(), self.txt_qtd_1.text(),
                        self.txt_precototal_1.text(),
                        max(dados_lancamento, key=int) + 1)

        dados_linha2 = (self.txt_cod_2.text(), self.txt_produto_2.text(),
                        self.txt_preco_2.text(), self.txt_qtd_2.text(),
                        self.txt_precototal_2.text(),
                        max(dados_lancamento, key=int) + 1)

        dados_linha3 = (self.txt_cod_3.text(), self.txt_produto_3.text(),
                        self.txt_preco_3.text(), self.txt_qtd_3.text(),
                        self.txt_precototal_3.text(),
                        max(dados_lancamento, key=int) + 1)

        dados_linha4 = (self.txt_cod_4.text(), self.txt_produto_4.text(),
                        self.txt_preco_4.text(), self.txt_qtd_4.text(),
                        self.txt_precototal_4.text(),
                        max(dados_lancamento, key=int) + 1)

        dados_linha5 = (self.txt_cod_5.text(), self.txt_produto_5.text(),
                        self.txt_preco_5.text(), self.txt_qtd_5.text(),
                        self.txt_precototal_5.text(),
                        max(dados_lancamento, key=int) + 1)

        dados_linha6 = (self.txt_cod_6.text(), self.txt_produto_6.text(),
                        self.txt_preco_6.text(), self.txt_qtd_6.text(),
                        self.txt_precototal_6.text(),
                        max(dados_lancamento, key=int) + 1)

        dados_linha7 = (self.txt_cod_7.text(), self.txt_produto_7.text(),
                        self.txt_preco_7.text(), self.txt_qtd_7.text(),
                        self.txt_precototal_7.text(),
                        max(dados_lancamento, key=int) + 1)


###### LIMPEZA DE CAMPOS LINEDIT DA TELA DE VENDAS ############################

        # LIMPEZA DE CAMPOS LINHA 01
        self.txt_cod_1.clear()
        self.txt_produto_1.clear()
        self.txt_preco_1.clear()
        self.txt_qtd_1.clear()
        self.txt_precototal_1.clear()

        # LIMPEZA DE CAMPOS LINHA 02
        self.txt_cod_2.clear()
        self.txt_produto_2.clear()
        self.txt_preco_2.clear()
        self.txt_qtd_2.clear()
        self.txt_precototal_2.clear()

        # LIMPEZA DE CAMPOS LINHA 03
        self.txt_cod_3.clear()
        self.txt_produto_3.clear()
        self.txt_preco_3.clear()
        self.txt_qtd_3.clear()
        self.txt_precototal_3.clear()

        # LIMPEZA DE CAMPOS LINHA 04
        self.txt_cod_4.clear()
        self.txt_produto_4.clear()
        self.txt_preco_4.clear()
        self.txt_qtd_4.clear()
        self.txt_precototal_4.clear()

        # LIMPEZA DE CAMPOS LINHA 05
        self.txt_cod_5.clear()
        self.txt_produto_5.clear()
        self.txt_preco_5.clear()
        self.txt_qtd_5.clear()
        self.txt_precototal_5.clear()

        # LIMPEZA DE CAMPOS LINHA 06
        self.txt_cod_6.clear()
        self.txt_produto_6.clear()
        self.txt_preco_6.clear()
        self.txt_qtd_6.clear()
        self.txt_precototal_6.clear()

        # LIMPEZA DE CAMPOS LINHA 07
        self.txt_cod_7.clear()
        self.txt_produto_7.clear()
        self.txt_preco_7.clear()
        self.txt_qtd_7.clear()
        self.txt_precototal_7.clear()

        # LIMPEZA DE CAMPOS LATERAL
        self.lineEdit_valor_total_2.clear()
        self.lineEdit_forma_pg_2.clear()
        self.lineEdit_valor_pago_2.clear()
        self.lineEdit_troco_2.clear()


###############################################################################

####### REPASSANDO DADOS DO LINEEDIT PARA O BANCO DE DADOS ####################

        # LINHA 01
        db.venda_produto(
            dados_linha1[0], dados_linha1[1], dados_linha1[2][3:],
            dados_linha1[3], dados_linha1[4][3:], dados_linha1[5])

        # LINHA 02
        if dados_linha2[1] == '':
            pass
        else:
            db.venda_produto(
                dados_linha2[0], dados_linha2[1], dados_linha2[2][3:],
                dados_linha2[3], dados_linha2[4][3:], dados_linha2[5])

        # LINHA 03
        if dados_linha3[1] == '':
            pass
        else:
            db.venda_produto(
                dados_linha3[0], dados_linha3[1], dados_linha3[2][3:],
                dados_linha3[3], dados_linha3[4][3:], dados_linha3[5])

        # LINHA 04
        if dados_linha4[1] == '':
            pass
        else:
            db.venda_produto(
                dados_linha4[0], dados_linha4[1], dados_linha4[2][3:],
                dados_linha4[3], dados_linha4[4][3:], dados_linha4[5])

        # LINHA 05
        if dados_linha5[1] == '':
            pass
        else:
            db.venda_produto(
                dados_linha5[0], dados_linha5[1], dados_linha5[2][3:],
                dados_linha5[3], dados_linha5[4][3:], dados_linha5[5])

        # LINHA 06
        if dados_linha6[1] == '':
            pass
        else:
            db.venda_produto(
                dados_linha6[0], dados_linha6[1], dados_linha6[2][3:],
                dados_linha6[3], dados_linha6[4][3:], dados_linha6[5])

        # LINHA 07
        if dados_linha7[1] == '':
            pass
        else:
            db.venda_produto(
                dados_linha7[0], dados_linha7[1], dados_linha7[2][3:],
                dados_linha7[3], dados_linha7[4][3:], dados_linha7[5])

        # CONFIGURAÇÃO PARA REPASSE DO VALOR TOTAL DOS ITENS #################

        # LINHA 01
        if dados_linha1[4][3:] == '':
            soma_lin1 = 0
        else:
            soma_lin1 = dados_linha1[4][3:]

        # LINHA 02
        if dados_linha2[4][3:] == '':
            soma_lin2 = 0
        else:
            soma_lin2 = dados_linha2[4][3:]

        # LINHA 03
        if dados_linha3[4][3:] == '':
            soma_lin3 = 0
        else:
            soma_lin3 = dados_linha3[4][3:]

        # LINHA 04
        if dados_linha4[4][3:] == '':
            soma_lin4 = 0
        else:
            soma_lin4 = dados_linha4[4][3:]

        # LINHA 05
        if dados_linha5[4][3:] == '':
            soma_lin5 = 0
        else:
            soma_lin5 = dados_linha5[4][3:]

        # LINHA 06
        if dados_linha6[4][3:] == '':
            soma_lin6 = 0
        else:
            soma_lin6 = dados_linha6[4][3:]

        # LINHA 07
        if dados_linha7[4][3:] == '':
            soma_lin7 = 0
        else:
            soma_lin7 = dados_linha7[4][3:]

        valor_conta = float(soma_lin1) + float(soma_lin2) + float(soma_lin3) + float(
            soma_lin4) + float(soma_lin5) + float(soma_lin6) + float(soma_lin7)

        ######################################################################
        dados_venda = (max(dados_lancamento, key=int) +
                       1, valor_conta, f_pg)
        db.registro_lancamento(
            dados_venda[0], dados_venda[1], dados_venda[2])


if __name__ == '__main__':
    db = data_base
    qt = QApplication(sys.argv)
    venda = Vendas()
    venda.show()
    qt.exec_()
