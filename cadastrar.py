import customtkinter as ctk #pip install customtkinter
import mysql.connector as my #pip install mysql-connector-python
from mysql.connector import errorcode
from datetime import date
from classbd import BancoDeDados

    #BANCO DE DADOS
class Cadastrar:

    def __init__(self):
        BancoDeDados().connectarbd()
        

        #INTERFACE GRÁFICA
        janela = ctk.CTk()
        janela.title("Cadastro de ITEM")

        labelInicio = ctk.CTkLabel(janela, text="Cadastre o ITEM: ").grid(row=0, column=1, pady=20, padx=20)
        labelConexao = ctk.CTkLabel(janela, text=BancoDeDados().connectarbd()).grid(row=0, column=2, pady=20, padx=20)
        labelSql = ctk.CTkLabel(janela, text="").grid(row=6, column=1, pady=20, padx=20)

        #labelId = ctk.CTkLabel(janela, text="ID: ").grid(row=1, column=1,padx=10, pady=10)
        #caixaId = ctk.CTkEntry(janela, placeholder_text="Digite o ID")
        #caixaId.grid(row=1, column=2,padx=10, pady=10)

        labelNome = ctk.CTkLabel(janela, text="NOME: ").grid(row=1, column=1,padx=10, pady=10)
        caixaNome = ctk.CTkEntry(janela, placeholder_text="Digite o Nome")
        caixaNome.grid(row=1, column=2,padx=10, pady=10)

        labelNome = ctk.CTkLabel(janela, text="MARCA: ").grid(row=2, column=1,padx=10, pady=10)
        caixaMarca = ctk.CTkEntry(janela, placeholder_text="Digite a Marca")
        caixaMarca.grid(row=2, column=2,padx=10, pady=10)

        labelEspecificacao = ctk.CTkLabel(janela, text="ESPECIFICAÇÃO: ").grid(row=3, column=1,padx=10, pady=10)
        caixaEspecificacao = ctk.CTkEntry(janela, placeholder_text="Digite a Especificação")
        caixaEspecificacao.grid(row=3, column=2,padx=10, pady=10)

        labelQuantidade = ctk.CTkLabel(janela, text="QUANTIDADE: ").grid(row=4, column=1,padx=10, pady=10)
        caixaQuantidade = ctk.CTkEntry(janela, placeholder_text="Digite a Quatidade")
        caixaQuantidade.grid(row=4, column=2,padx=10, pady=10)

        botaoCadastrar = ctk.CTkButton(janela, text="Cadastrar", command=BancoDeDados().cadastrar_criarTabela()).grid(row=5, column=2,padx=10, pady=10)
        botaoSair = ctk.CTkButton(janela, text="Sair",command=janela.destroy).grid(row=5, column=1,padx=10, pady=10)


        janela.geometry("350x350")
        janela.resizable(0,0)
        janela.mainloop()


iniciar = Cadastrar()
print(iniciar)