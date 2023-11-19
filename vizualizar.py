import customtkinter as ctk
from tkinter import ttk
import tkinter as tk
from tkinter.messagebox import showinfo
import mysql.connector as my #pip install mysql-connector-python
from mysql.connector import errorcode



def vizualizar():

    def deletar():
        sql_delete = '''DELETE FROM ESTOQUE WHERE ID = %s'''
        valor_para_deletar = deletar_entry.get()
        cursor.execute(sql_delete, (valor_para_deletar,))
        db_connection.commit()
        print(f'Registro com o ID {sql_delete} foi deletado com sucesso!')

    #alterar dados do registro
    def item_selected(event):
        for selected_item in tree.selection():
            item = tree.item(selected_item)
            record = item['values']

        janela2 = ctk.CTk()

        def atualizar():
            #alterar valores no banco de dados
            sql = "UPDATE ESTOQUE SET NOME = %s, MARCA = %s, ESPECIFICACAO = %s, QUANTIDADE = %s "
            valores = nomeentry.get(),marcaentry.get(),especientry.get(),qtdentry.get()
            cursor.execute(sql, valores)
            db_connection.commit()
            print('Os dados foram atualizados!')


            #atualizar a vizualização dos registros
            
            vizualizar()
  

        nomeentry = ctk.CTkEntry(janela2)
        nomeentry.insert(0, record[1])
        nomeentry.grid(row=0, column=1,padx=10, pady=10)
        nomelabel = ctk.CTkLabel(janela2, text='NOME: ').grid(row=0, column=0, padx=10, pady=10)

        marcaentry = ctk.CTkEntry(janela2)
        marcaentry.insert(0, record[2])
        marcaentry.grid(row=1, column=1, padx=10, pady=10)
        marcalabel = ctk.CTkLabel(janela2, text='MARCA: ').grid(row=1, column=0, padx=10, pady=10)

        especientry = ctk.CTkEntry(janela2)
        especientry.insert(0, record[3])
        especientry.grid(row=2, column=1, padx=10, pady=10)
        especilabel = ctk.CTkLabel(janela2, text='ESPECIFICAÇÃO: ').grid(row=2, column=0, padx=10, pady=10)

        qtdentry = ctk.CTkEntry(janela2)
        qtdentry.insert(0, record[4])
        qtdentry.grid(row=3, column=1, padx=10, pady=10)
        qtdlabel = ctk.CTkLabel(janela2, text='QUANTIDADE: ').grid(row=3, column=0,padx=10, pady=10)

        botaoAtualiza = ctk.CTkButton(janela2, text='Atualizar', command=atualizar).grid(row=4, column=0, padx=10, pady=10)
        botaoSair = ctk.CTkButton(janela2, text='Sair', command=janela2.destroy).grid(row=4, column=1, padx=10, pady=10)
    


        janela2.title('Alterar dados do registro')
        janela2.geometry("350x250")
        janela2.resizable(0,0)
        janela2.mainloop()   


    #conexão com banco de dados
    try:
        db_connection = my.connect(host='localhost', user='root',password='123456', database='bd',)
        conexao = "Conexão estabelecida!"
        cursor = db_connection.cursor()

    except my.Error as error:
        if error.errno == errorcode.ER_BAD_DB_ERROR:
            conexao = "O Banco de Dados não existe!"
        elif error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            conexao = "Usário ou Senha está errada!"
        else:
            conexao = error
    print(conexao)
    sql_select_query = '''SELECT * FROM ESTOQUE'''
    cursor.execute(sql_select_query)
    registros = cursor.fetchall()

        
    janela = ctk.CTk()

    colunas = ("ID", "NOME", "MARCA", "ESPECIFICACAO", "QUANTIDADE")

    tree = ttk.Treeview(janela, columns=colunas,show = "headings")


    tree.heading("ID", text="ID")
    tree.heading("NOME", text="NOME")
    tree.heading("MARCA", text="MARCA")
    tree.heading("ESPECIFICACAO", text="ESPECIFICACAO")
    tree.heading("QUANTIDADE", text="QUANTIDADE")


    contacts = registros
    

    for contact in contacts:
        tree.insert('', tk.END, values=contact)

    


    tree.bind('<<TreeviewSelect>>', item_selected)

    

    # add a scrollbar
    scrollbar = ttk.Scrollbar(janela, orient=tk.VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrollbar.set)


    
    deletar_por_id = ctk.CTkButton(janela, text='DELETAR', command=deletar)
    deletar_entry = ctk.CTkEntry(janela, placeholder_text='DIGITE O ID')

    tree.grid(row=0, column=0, sticky='nsew')
    scrollbar.grid(row=0, column=1, sticky='ns')
    deletar_por_id.place(x=150,y=230)
    deletar_entry.place(x=0,y=230)

    janela.title("Vizualizar e Editar o Estoque")
    janela.geometry("1020x350")
    janela.resizable(0,0)
    janela.mainloop()

vizualizar()