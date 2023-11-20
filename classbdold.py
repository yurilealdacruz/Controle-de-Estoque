import mysql.connector as my #pip install mysql-connector-python
from mysql.connector import errorcode
from datetime import date



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
        registros = []
        try:
            cursor = self.db_connection.cursor()
            print('Selecionando todos os produtos')
            sql_select_query = '''SELECT * FROM ESTOQUE'''
            cursor.execute(sql_select_query)
            registros = self.cursor.fetchall()
            print(registros)

        except (Exception, my.Error) as erro:
            print('Ocorreu um erro e não foi possível selecionar a tabela, erro: ',erro)

        finally:
            if self.db_connection.is_connected():
                cursor.close()
        
        return registros

    def cadastrar_criarTabela(self, nome, marca, especificacao, quantidade):
        try:
            sql = "INSERT INTO ESTOQUE VALUES (NULL, %s, %s, %s, %s)"
            valores = (nome, marca, especificacao, quantidade)
            cursor.execute(sql, valores)
            self.db_connection.commit()
            print('Os dados foram inseridos!')
        except my.Error as erro:
            if erro.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print('A tabela já existe.')
            else:
                print(f'Ocorreu um erro: {erro}')


    def criar_tabela(self):
        tabela = """
        CREATE TABLE ESTOQUE (
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

