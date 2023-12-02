import customtkinter as ctk #pip install customtkinter
from cadastrar import Cadastrar
from vizualizar import Vizualizar
#import vizualizar

class Tela:
    def __init__(self):

        def cadastrar_item():
            return Cadastrar()
        
        def vizualizar():
            return Vizualizar()
        
        janela = ctk.CTk()
        janela.title("Opções do controle de Estoque")

        ctk.CTkLabel(janela, text="Escolha uma das opções: ")

        labelEstoque = ctk.CTkLabel(janela, text="Controle de Estoque")
        ctk.CTkLabel(janela, text="Controle de Salas")


        botaoCadastro = ctk.CTkButton(janela, text="Cadastrar", command=cadastrar_item)
        botaoAtualizar = ctk.CTkButton(janela, text="Vizualizar / Atualizar", command=vizualizar)

        labelEstoque.place(x=120, y=20)
        botaoCadastro.place(x=110, y=70)
        botaoAtualizar.place(x=110, y=120)

        janela.geometry("350x190")
        janela.resizable(0,0)
        janela.mainloop()