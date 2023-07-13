from models.Assunto import Assunto
from views.Ico import Ico
import tkinter as tk

class EdicaoDeAssuntoView:

    def __init__(self, assunto: Assunto) -> None:
        self. assunto = assunto
        color = '#404040'

        self.janela = tk.Tk()
        title = f'Gerenciador de Favoritos - Edição do Assunto {assunto.nome}'
        self.janela.title(title)
        self.janela.configure(bg=color)
        largura_tela = self.janela.winfo_screenwidth()
        altura_tela = self.janela.winfo_screenheight()
        self.janela.geometry(f"{largura_tela}x{altura_tela}+0+0")

        self.frame = tk.Frame(self.janela)
        self.frame.configure(bg=color)
        self.frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.edicao_frame = tk.Frame(self.frame)
        self.edicao_frame.configure(bg=color)
        self.edicao_frame.grid(row=0, column=0, padx=16, pady=16)

        self.id_label = tk.Label(
            self.edicao_frame,
            bg=color,
            fg='white',
            text='Id',
            font=('serif', 16)
        )
        self.id_label.grid(row=0, column=0, padx=16, pady=16)

        self.id_entry = tk.Label(
            self.edicao_frame,
            bg=color,
            fg='white',
            text=str(assunto.id),
            font=('serif', 16)
        )
        self.id_entry.grid(row=0, column=1, padx=16, pady=16)

        self.assunto_label = tk.Label(
            self.edicao_frame,
            bg=color,
            fg='white',
            text='Assunto',
            font=('serif', 16)
        )
        self.assunto_label.grid(row=1, column=0, padx=16, pady=16)

        self.assunto_entry = tk.Entry(
            self.edicao_frame,
            font=('serif', 16)
        )
        self.assunto_entry.insert(0, assunto.nome)
        self.assunto_entry.grid(row=1, column=1, padx=16, pady=16)

        self.button_frame = tk.Frame(self.frame)
        self.button_frame.configure(bg=color)
        self.button_frame.grid(row=1, column=0, padx=16, pady=16)
        
        self.atualizar_button = tk.Button(
            self.button_frame,
            bg=color,
            fg='white',
            font=('serif', 16),
            text='Atualizar',
            command=self.atualizar
        )
        self.atualizar_button.grid(row=0, column=0, padx=16, pady=16)

        Ico(self.janela).mostrar()
        self.janela.attributes('-zoomed', True)
        self.janela.mainloop()
    
    def atualizar(self) -> None:
        from controllers.AssuntoController import AssuntoController
        id = self.assunto.id
        nome = self.assunto_entry.get()
        self.janela.destroy()
        AssuntoController().atualizar(id, nome)