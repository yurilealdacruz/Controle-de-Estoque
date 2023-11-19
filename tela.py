import customtkinter as ctk #pip install customtkinter

def tela():
#FUNÇÕES
    def cadastrar_item():
        import cadastrar
        return cadastrar.cadastrarr()
    def vizualizar():
        import vizualizar
        return vizualizar.vizualizar()

    #INTERFACE GRÁFICA
    janela = ctk.CTk()
    janela.title("Opções do controle de Estoque")

    labelInicio = ctk.CTkLabel(janela, text="Escolha uma das opções: ")

    labelEstoque = ctk.CTkLabel(janela, text="Controle de Estoque")
    labelSalas = ctk.CTkLabel(janela, text="Controle de Salas")


    botaoCadastro = ctk.CTkButton(janela, text="Cadastrar", command=cadastrar_item)
    botaoAtualizar = ctk.CTkButton(janela, text="Vizualizar / Atualizar", command=vizualizar)

    labelEstoque.place(x=120, y=20)
    botaoCadastro.place(x=110, y=70)
    botaoAtualizar.place(x=110, y=120)

    janela.geometry("350x190")
    janela.resizable(0,0)
    janela.mainloop()
tela()