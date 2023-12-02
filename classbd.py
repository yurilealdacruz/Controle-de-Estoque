import mysql.connector as my #pip install mysql-connector-python
from mysql.connector import errorcode

class BancoDeDados:

    def __init__(self):
        self.connectarbd()

    def connectarbd(self):
        try:
            self.db_connection = my.connect(host='localhost', user='root', password='13579', database='bd')
            self.cursor = self.db_connection.cursor()
            self.conexao = "Conexão estabelecida!"

        except my.Error as error:
            if error.errno == errorcode.ER_BAD_DB_ERROR:
                self.conexao = "O Banco de Dados não existe!"
            elif error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                self.conexao = "Usuário ou Senha está errada!"
            else:
                self.conexao = error

        return self.conexao

    def mostrar_registros(self):
        self.connectarbd()
        registros = []
        try:
            sql_select_query = '''SELECT * FROM ESTOQUE'''
            self.cursor.execute(sql_select_query)
            registros = self.cursor.fetchall()

        except (Exception, my.Error) as erro:
            print('Ocorreu um erro e não foi possível selecionar a tabela, erro: ', erro)

        finally:
            if self.db_connection.is_connected():
                self.cursor.close()

        return registros

    def cadastrar_criarTabela(self, nome, marca, especificacao, quantidade):
        try:
            sql = "INSERT INTO ESTOQUE VALUES (NULL, %s, %s, %s, %s)"
            valores = (nome, marca, especificacao, quantidade)
            self.cursor.execute(sql, valores)
            self.db_connection.commit()
            print('Os dados foram inseridos!')
        except my.Error as erro:
            if erro.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print('A tabela já existe.')
            else:
                print(f'Ocorreu um erro: {erro}')
                print('A tabela está sendo criada...')
                self.criar_tabela()

    
    def atualizar(self, nome, marca, especificacao, quantidade, id_reg):
        try:
            self.connectarbd()  # Certifica-se de que a conexão está aberta
            # Altera os valores no banco de dados
            sql = "UPDATE ESTOQUE SET NOME = %s, MARCA = %s, ESPECIFICACAO = %s, QUANTIDADE = %s WHERE ID = %s"
            valores = (nome, marca, especificacao, quantidade, id_reg)
            self.cursor.execute(sql, valores)
            self.db_connection.commit()
            print('Os dados foram atualizados')

        except my.Error as erro:
            print(f'Ocorreu um erro: {erro}')

        finally:
            # Fecha o cursor e a conexão
            if self.db_connection.is_connected():
                self.cursor.close()
                self.db_connection.close()
    def criar_tabela(self):
        tabela = """
        CREATE TABLE IF NOT EXISTS ESTOQUE (
        ID INT AUTO_INCREMENT,
        NOME TEXT NOT NULL,
        MARCA TEXT NOT NULL,
        ESPECIFICACAO TEXT NOT NULL,
        QUANTIDADE INT NOT NULL,
        PRIMARY KEY (ID)
        );
        """
        self.cursor.execute(tabela)
        self.db_connection.commit()
        print('TABELA CRIADA!')

    def deletar(self, id_capturado):
        self.connectarbd()
        sql_delete = '''DELETE FROM ESTOQUE WHERE ID = %s'''
        valor_para_deletar = id_capturado
        self.cursor.execute(sql_delete, (valor_para_deletar,))
        self.db_connection.commit()
        print(f'Registro com o ID {id_capturado} foi deletado com sucesso!')
        self.db_connection.close()

    def recuperar_registros(self):
        sql_select_query = '''SELECT * FROM ESTOQUE'''
        self.cursor.execute(sql_select_query)
        registros = self.cursor.fetchall()
