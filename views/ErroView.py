from views.Ico import Ico
import tkinter as tk

class ErroView:

    def __init__(self, mensagem_erro: str) -> None:
        color = '#BF4040'

        self.janela = tk.Tk()
        self.janela.title('Gerenciador de Favoritos - Erro')
        self.janela.configure(bg=color)
        largura_tela = self.janela.winfo_screenwidth()
        altura_tela = self.janela.winfo_screenheight()
        self.janela.geometry(f"{largura_tela}x{altura_tela}+0+0")

        self.frame = tk.Frame(self.janela)
        self.frame.configure(bg=color)
        self.frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.label_frame = tk.Frame(self.frame)
        self.label_frame.configure(bg=color)
        self.label_frame.grid(row=0, column=0, padx=16, pady=16)

        self.label = tk.Label(
            self.label_frame,
            bg=color,
            fg='white',
            text=mensagem_erro,
            font=('serif', 16)
        )
        self.label.grid(row=0, column=0, padx=16, pady=16)

        self.buttons_frame = tk.Frame(self.frame)
        self.buttons_frame.configure(bg=color)
        self.buttons_frame.grid(row=1, column=0, padx=16, pady=16)
        
        self.assuntos_button = tk.Button(
            self.buttons_frame,
            bg=color,
            fg='white',
            font=('serif', 16),
            text='Listar Assuntos',
            command=self.abrir_assuntos
        )
        self.assuntos_button.grid(row=0, column=0, padx=16, pady=16)
        
        self.sair_button = tk.Button(
            self.buttons_frame,
            bg=color,
            fg='white',
            font=('serif', 16),
            text='Fechar',
            command=self.fechar
        )
        self.sair_button.grid(row=0, column=1, padx=16, pady=16)

        Ico(self.janela).mostrar()
        self.janela.attributes('-zoomed', True)
        self.janela.mainloop()

    def abrir_assuntos(self) -> None:
        from controllers.AssuntoController import AssuntoController
        self.janela.destroy()
        AssuntoController().listar()

    def fechar(self) -> None:
        self.janela.destroy()