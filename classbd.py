import mysql.connector as my #pip install mysql-connector-python
from mysql.connector import errorcode
from datetime import date

class BancoDeDados:

    def __init__(self):
        ...
    def connectarbd(self):
        try:
            self.db_connection = my.connect(host='localhost', user='root',password='13579', database='bd',)
            self.conexao = "Conexão estabelecida!"
        
        except my.Error as error:
            if error.errno == errorcode.ER_BAD_DB_ERROR:
                self.conexao = "O Banco de Dados não existe!"
            elif error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                self.conexao = "Usário ou Senha está errada!"
            else:
                self.conexao = error
        
        return self.conexao
    def mostrar_registros(self):
        try:
            self.connectarbd()
            cursor = self.db.connection.cursor()
            print('Selecionando todos os produtos')
            sql_select_query = '''SELECT * FROM ESTOQUE'''
            cursor.execute(sql_select_query)
            registros = cursor.fetchall()
            print(registros)

        except (Exception, my.Error) as erro:
            print('Ocorreu um erro e não foi possível selecionar a tabela, erro: ',erro)

        finally:
            if (self.db_connection):
                cursor.close()
                self.db_connection.close()
                print('A conexão com o MySQL foi encerrada')
        
        return registros

    def cadastrar_criarTabela(self, cauxaNome, CaixaMarca, CaixaEspecificacao, CaixaQuantidade):
            try:
                self.connectarbd()
                cursor = self.db_connection.cursor()
                sql = "INSERT INTO ESTOQUE VALUES (NULL, %s, %s, %s, %s)"
                valores = (caixaNome, caixaMarca, caixaEspecificacao, caixaQuantidade)
                cursor.execute(sql, valores)
                self.db_connection.commit()
                print('Os dados foram inseridos!')
            except:
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
                cursor.execute(tabela)
                self.db_connection.commit()
                print('TABELA CRIADA!')
            finally:
                if (self.db_connection):
                    cursor.close()
                    self.db_connection.close()
                    print('A conexao com o MySQL foi encerrada')

