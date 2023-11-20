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
        ctk.CTkLabel(janela, text="").grid(row=6, column=1, pady=20, padx=20)

        ctk.CTkLabel(janela, text="NOME: ").grid(row=1, column=1, padx=10, pady=10)
        caixaNome = ctk.CTkEntry(janela, placeholder_text="Digite o Nome")
        caixaNome.grid(row=1, column=2, padx=10, pady=10)

        ctk.CTkLabel(janela, text="MARCA: ").grid(row=2, column=1, padx=10, pady=10)
        caixaMarca = ctk.CTkEntry(janela, placeholder_text="Digite a Marca")
        caixaMarca.grid(row=2, column=2, padx=10, pady=10)

        ctk.CTkLabel(janela, text="ESPECIFICAÇÃO: ").grid(row=3, column=1, padx=10, pady=10)
        caixaEspecificacao = ctk.CTkEntry(janela, placeholder_text="Digite a Especificação")
        caixaEspecificacao.grid(row=3, column=2, padx=10, pady=10)

        ctk.CTkLabel(janela, text="QUANTIDADE: ").grid(row=4, column=1, padx=10, pady=10)
        caixaQuantidade = ctk.CTkEntry(janela, placeholder_text="Digite a Quantidade")
        caixaQuantidade.grid(row=4, column=2, padx=10, pady=10)

        botaoCadastrar = ctk.CTkButton(janela, text="Cadastrar", command=lambda: self.cadastrar(caixaNome, caixaMarca, caixaEspecificacao, caixaQuantidade)).grid(row=5, column=2, padx=10, pady=10)
        botaoSair = ctk.CTkButton(janela, text="Sair", command=janela.destroy).grid(row=5, column=1, padx=10, pady=10)

        janela.geometry("350x350")
        janela.resizable(0, 0)
        janela.mainloop()

    def cadastrar(self, caixaNome, caixaMarca, caixaEspecificacao, caixaQuantidade):
        nome = caixaNome.get()
        marca = caixaMarca.get()
        especificacao = caixaEspecificacao.get()
        quantidade = caixaQuantidade.get()

        self.bd.cadastrar_criarTabela(nome, marca, especificacao, quantidade)

# Exemplo de uso
iniciar = Cadastrar()