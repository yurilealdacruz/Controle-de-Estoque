import customtkinter as ctk #pip install customtkinter
import webbrowser

class Main:
    def __init__(self, win):
        # INTERFACE GRÁFICA
        ctk.set_appearance_mode("System")  
        ctk.set_default_color_theme("blue")

        self.textoPrincipal = ctk.CTkLabel(win, text="Realizar o Login: ")
        self.botaoLogin = ctk.CTkButton(win, text="Entrar", corner_radius=10, command=self.abrir_tela)
        self.caixaLogin = ctk.CTkEntry(win, placeholder_text="Digite seu Login")
        self.caixaSenha = ctk.CTkEntry(win, placeholder_text="Digite sua Senha", show="*")
        self.botaoInfo = ctk.CTkButton(win, text="Info", corner_radius=10,width=100, height=25 ,command=self.info)

        self.textoPrincipal.pack(padx=10, pady=10)
        self.caixaLogin.pack(padx=10, pady=10)
        self.caixaSenha.pack(padx=10, pady=10)
        self.botaoLogin.pack(padx=10, pady=10)
        self.botaoInfo.place(relx=0.76, rely=0.87)

    #FUNÇÕES
    def abrir_tela(self):
        if self.caixaLogin.get() == "Yuri" and self.caixaSenha.get() == "123":
            import tela
            janela.destroy()
            return tela.tela()
            
    def info():
        webbrowser.open("https://yurilealdacruz.github.io/")


janela = ctk.CTk()
printipal = Main(janela)
janela.title("Controle de Estoque")
janela.geometry("500x260")
janela.resizable(0,0)
janela.mainloop()