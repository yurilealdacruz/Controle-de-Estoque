import customtkinter as ctk
from tkinter import ttk
import tkinter as tk
from tkinter.messagebox import showinfo
from classbd import BancoDeDados

class Vizualizar:

    def __init__(self):
        self.bd = BancoDeDados()
        self.criar_interface()

    def deletar(self, deletar_entry):
        id_capturado = deletar_entry.get()
        self.bd.deletar(id_capturado)
        self.janela.destroy()
        Vizualizar()
        

    def atualizar(self, nomeentry, marcaentry, especientry, qtdentry, id_selecionado):
        nome = nomeentry.get()
        marca = marcaentry.get()
        especificacao = especientry.get()
        quantidade = qtdentry.get()
        id_reg = id_selecionado
        self.bd.atualizar(nome, marca, especificacao, quantidade, id_reg)
        self.janela.destroy()
        self.janela2.destroy()
        Vizualizar()
        
        

    #alterar dados do registro
    def item_selected(self, event):
        for selected_item in self.tree.selection():
            item = self.tree.item(selected_item)
            record = item['values']

        self.janela2 = ctk.CTk()

        nomeentry = ctk.CTkEntry(self.janela2)
        nomeentry.insert(0, record[1])
        nomeentry.grid(row=0, column=1,padx=10, pady=10)
        ctk.CTkLabel(self.janela2, text='NOME: ').grid(row=0, column=0, padx=10, pady=10)

        marcaentry = ctk.CTkEntry(self.janela2)
        marcaentry.insert(0, record[2])
        marcaentry.grid(row=1, column=1, padx=10, pady=10)
        ctk.CTkLabel(self.janela2, text='MARCA: ').grid(row=1, column=0, padx=10, pady=10)

        especientry = ctk.CTkEntry(self.janela2)
        especientry.insert(0, record[3])
        especientry.grid(row=2, column=1, padx=10, pady=10)
        ctk.CTkLabel(self.janela2, text='ESPECIFICAÇÃO: ').grid(row=2, column=0, padx=10, pady=10)

        qtdentry = ctk.CTkEntry(self.janela2)
        qtdentry.insert(0, record[4])
        qtdentry.grid(row=3, column=1, padx=10, pady=10)
        ctk.CTkLabel(self.janela2, text='QUANTIDADE: ').grid(row=3, column=0,padx=10, pady=10)

        id_selecionado = record[0]

        botaoAtualiza = ctk.CTkButton(self.janela2, text='Atualizar', command=lambda: self.atualizar(nomeentry, marcaentry, especientry, qtdentry, id_selecionado)).grid(row=4, column=0, padx=10, pady=10)
        botaoSair = ctk.CTkButton(self.janela2, text='Sair', command=self.janela2.destroy).grid(row=4, column=1, padx=10, pady=10)

        self.janela2.title('Alterar dados do registro')
        self.janela2.geometry("350x250")
        self.janela2.resizable(0,0)
        self.janela2.mainloop()   

    def criar_interface(self):
        self.janela = ctk.CTk()

        colunas = ("ID", "NOME", "MARCA", "ESPECIFICACAO", "QUANTIDADE")

        self.tree = ttk.Treeview(self.janela, columns=colunas,show = "headings")

        self.tree.heading("ID", text="ID")
        self.tree.heading("NOME", text="NOME")
        self.tree.heading("MARCA", text="MARCA")
        self.tree.heading("ESPECIFICACAO", text="ESPECIFICACAO")
        self.tree.heading("QUANTIDADE", text="QUANTIDADE")

        contacts = self.bd.mostrar_registros()
        
        for contact in contacts:
            self.tree.insert('', tk.END, values=contact)

        self.tree.bind('<<TreeviewSelect>>', self.item_selected)

        # add a scrollbar
        scrollbar = ttk.Scrollbar(self.janela, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)



        deletar_por_id = ctk.CTkButton(self.janela, text='DELETAR', command=lambda: self.deletar(self.deletar_entry))
        self.deletar_entry = ctk.CTkEntry(self.janela, placeholder_text='DIGITE O ID')

        self.tree.grid(row=0, column=0, sticky='nsew')
        scrollbar.grid(row=0, column=1, sticky='ns')
        deletar_por_id.place(x=150,y=230)
        self.deletar_entry.place(x=0,y=230)

        self.janela.title("Vizualizar e Editar o Estoque")
        self.janela.geometry("1020x300")
        self.janela.resizable(0,0)
        self.janela.mainloop()
