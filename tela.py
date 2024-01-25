import customtkinter as ctk #pip install customtkinter
from cadastrar import Cadastrar
from visualizar import Visualizar

class Tela:
    def __init__(self, janela: ctk.CTk):
        self.janela = janela
        self.janela.title("Opções do controle de Estoque")
        self.janela.geometry("350x190+700+325")

        ctk.CTkLabel(self.janela, text="Escolha uma das opções: ")

        labelEstoque = ctk.CTkLabel(self.janela, text="Controle de Estoque")
        ctk.CTkLabel(self.janela, text="Controle de Salas")

        botaoCadastro = ctk.CTkButton(self.janela, text="Cadastrar", command=self.cadastrar_item)
        botaoAtualizar = ctk.CTkButton(self.janela, text="Visualizar / Atualizar", command=self.visualizar)

        labelEstoque.place(x=120, y=20)
        botaoCadastro.place(x=110, y=70)
        botaoAtualizar.place(x=110, y=120)

    def cadastrar_item(self):
        return Cadastrar()
        
    def visualizar(self):
        return Visualizar()
