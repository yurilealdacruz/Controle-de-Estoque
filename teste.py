import customtkinter as ctk
from classbd import BancoDeDados

class Cadastrar:

    def __init__(self):
        self.bd = BancoDeDados()
        self.criar_interface()

    def criar_interface(self):
        janela = ctk.CTk()
        janela.title("Cadastro de ITEM")

        ctk.CTkLabel(janela, text="Cadastre o ITEM: ").grid(row=0, column=1, pady=20, padx=20)
        ctk.CTkLabel(janela, text=self.bd.connectarbd()).grid(row=0, column=2, pady=20, padx=20)

        # Restante do código de criação da interface...

        botaoCadastrar = ctk.CTkButton(janela, text="Cadastrar", command=self.cadastrar).grid(row=5, column=2, padx=10, pady=10)
        botaoSair = ctk.CTkButton(janela, text="Sair", command=janela.destroy).grid(row=5, column=1, padx=10, pady=10)

        janela.geometry("350x350")
        janela.resizable(0, 0)
        janela.mainloop()

    def cadastrar(self):
        # Restante do código para obter valores dos campos de entrada...
        self.bd.nome = caixaNome.get()
        self.bd.marca = caixaMarca.get()
        self.bd.especificacao = caixaEspecificacao.get()
        self.bd.quantidade = caixaQuantidade.get()

        self.bd.cadastrar_criarTabela()

# Exemplo de uso
iniciar = Cadastrar()