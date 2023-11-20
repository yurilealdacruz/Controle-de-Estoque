import customtkinter as ctk #pip install customtkinter
import mysql.connector as my #pip install mysql-connector-python
from mysql.connector import errorcode
from datetime import date
from classbd import BancoDeDados

    #BANCO DE DADOS
class Cadastrar:

    def __init__(self):
        self.bd = BancoDeDados()
        self.criar_interface()

        
    def criar_interface(self):
        janela = ctk.CTk()
        janela.title("Cadastro de ITEM")

        ctk.CTkLabel(janela, text="Cadastre o ITEM: ").grid(row=0, column=1, pady=20, padx=20)
        ctk.CTkLabel(janela, text=self.bd.connectarbd()).grid(row=0, column=2, pady=20, padx=20)
        ctk.CTkLabel(janela, text="").grid(row=6, column=1, pady=20, padx=20)

        ctk.CTkLabel(janela, text="NOME: ").grid(row=1, column=1,padx=10, pady=10)
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

        botaoCadastrar = ctk.CTkButton(janela, text="Cadastrar", command=self.cadastrar()).grid(row=5, column=2,padx=10, pady=10)
        botaoSair = ctk.CTkButton(janela, text="Sair",command=janela.destroy).grid(row=5, column=1,padx=10, pady=10)

        janela.geometry("350x350")
        janela.resizable(0,0)
        janela.mainloop()

       def cadastrar(self):
        # Restante do código para obter valores dos campos de entrada...
        self.bd.nome = caixaNome.get()
        self.bd.marca = caixaMarca.get()
        self.bd.especificacao = caixaEspecificacao.get()
        self.bd.quantidade = caixaQuantidade.get()

        self.bd.cadastrar_criarTabela()

