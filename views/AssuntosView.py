from models.Assunto import Assunto
from views.Ico import Ico
import tkinter as tk

class AssuntosView:

    def __init__(self, assuntos: list[Assunto]) -> None:
        color = '#404040'

        self.janela = tk.Tk()
        self.janela.title('Gerenciador de Favoritos - Escolha um Assunto')
        self.janela.configure(bg=color)
        largura_tela = self.janela.winfo_screenwidth()
        altura_tela = self.janela.winfo_screenheight()
        self.janela.geometry(f"{largura_tela}x{altura_tela}+0+0")

        self.frame = tk.Frame(self.janela)
        self.frame.configure(bg=color)
        self.frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        if assuntos:
            self.label = tk.Label(
                self.frame,
                bg=color,
                fg='white',
                text='Selecione um assunto',
                font=('serif', 16)
            )
            self.label.grid(row=0, column=0, padx=16, pady=16)

            self.nomes_do_assuntos = [(assunto.nome) for assunto in assuntos]
            self.combo = tk.StringVar(self.frame)
            self.combo.set(self.nomes_do_assuntos[0])
            self.seletor = tk.OptionMenu(
                self.frame,
                self.combo,
                *self.nomes_do_assuntos
            )
            self.seletor.configure(bg=color, fg='white', font=('serif', 16))
            self.seletor.grid(row=0, column=1, padx=16, pady=16)
            
            self.editar_assunto_button = tk.Button(
                self.frame,
                bg=color,
                fg='white',
                font=('serif', 16),
                text='Editar Assunto',
                command=self.corrigir
            )
            self.editar_assunto_button.grid(row=0, column=2, padx=16, pady=16)
            
            self.favoritosButton = tk.Button(
                self.frame,
                bg=color,
                fg='white',
                font=('serif', 16),
                text='Listar Favoritos',
                command=self.listarFavoritos
            )
            self.favoritosButton.grid(row=0, column=3, padx=16, pady=16)
        
        self.criar_favorito_button = tk.Button(
            self.frame,
            bg=color,
            fg='white',
            font=('serif', 16),
            text='Inserir Favorito',
            command=self.inserirFavorito
        )
        self.criar_favorito_button.grid(row=0, column=4, padx=16, pady=16)

        Ico(self.janela).mostrar()
        self.janela.attributes('-zoomed', True)
        self.janela.mainloop()

    def corrigir(self) -> None:
        from controllers.AssuntoController import AssuntoController
        assunto = self.combo.get()
        self.janela.destroy()
        AssuntoController().editar(assunto)
    
    def listarFavoritos(self) -> None:
        from controllers.FavoritoController import FavoritoController
        assunto = self.combo.get()
        self.janela.destroy()
        FavoritoController().listar(assunto)
    
    def inserirFavorito(self) -> None:
        from controllers.FavoritoController import FavoritoController
        self.janela.destroy()
        FavoritoController().criar()
