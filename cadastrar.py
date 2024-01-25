import customtkinter as ctk
from classbd import BancoDeDados

class Cadastrar:

    def __init__(self):
        self.janela = ctk.CTkToplevel()
        self.janela.title("Cadastro de ITEM")
        self.janela.geometry("350x350+340+165")
        self.janela.resizable(0, 0)
        
        self.bd = BancoDeDados()      
        self.criar_interface()

    def criar_interface(self):
        ctk.CTkLabel(self.janela, text="Cadastre o ITEM: ").grid(row=0, column=1, pady=20, padx=20)
        ctk.CTkLabel(self.janela, text=self.bd.connectarbd()).grid(row=0, column=2, pady=20, padx=20)
        ctk.CTkLabel(self.janela, text="").grid(row=6, column=1, pady=20, padx=20)

        ctk.CTkLabel(self.janela, text="NOME: ").grid(row=1, column=1, padx=10, pady=10)
        caixaNome = ctk.CTkEntry(self.janela, placeholder_text="Digite o Nome")
        caixaNome.grid(row=1, column=2, padx=10, pady=10)

        ctk.CTkLabel(self.janela, text="MARCA: ").grid(row=2, column=1, padx=10, pady=10)
        caixaMarca = ctk.CTkEntry(self.janela, placeholder_text="Digite a Marca")
        caixaMarca.grid(row=2, column=2, padx=10, pady=10)

        ctk.CTkLabel(self.janela, text="ESPECIFICAÇÃO: ").grid(row=3, column=1, padx=10, pady=10)
        caixaEspecificacao = ctk.CTkEntry(self.janela, placeholder_text="Digite a Especificação")
        caixaEspecificacao.grid(row=3, column=2, padx=10, pady=10)

        ctk.CTkLabel(self.janela, text="QUANTIDADE: ").grid(row=4, column=1, padx=10, pady=10)
        caixaQuantidade = ctk.CTkEntry(self.janela, placeholder_text="Digite a Quantidade")
        caixaQuantidade.grid(row=4, column=2, padx=10, pady=10)

        botaoCadastrar = ctk.CTkButton(self.janela, text="Cadastrar", command=lambda: self.cadastrar(caixaNome, caixaMarca, caixaEspecificacao, caixaQuantidade)).grid(row=5, column=2, padx=10, pady=10)
        botaoSair = ctk.CTkButton(self.janela, text="Sair", command=self.janela.destroy).grid(row=5, column=1, padx=10, pady=10)

    def cadastrar(self, caixaNome, caixaMarca, caixaEspecificacao, caixaQuantidade):
        nome = caixaNome.get()
        marca = caixaMarca.get()
        especificacao = caixaEspecificacao.get()
        quantidade = caixaQuantidade.get()

        self.bd.cadastrar_criarTabela(nome, marca, especificacao, quantidade)
