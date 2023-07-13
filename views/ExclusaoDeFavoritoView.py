from models.Favorito import Favorito
from views.Ico import Ico
import tkinter as tk

class ExclusaoDeFavoritoView:

    def __init__(self, favorito: Favorito) -> None:
        self.favorito = favorito
        color = '#BF8040'

        self.janela = tk.Tk()
        self.janela.title('Gerenciador de Favoritos - Exclusão de Favorito')
        self.janela.configure(bg=color)
        largura_tela = self.janela.winfo_screenwidth()
        altura_tela = self.janela.winfo_screenheight()
        self.janela.geometry(f"{largura_tela}x{altura_tela}+0+0")

        self.frame = tk.Frame(self.janela)
        self.frame.configure(bg=color)
        self.frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.informacoes_frame = tk.Frame(self.frame)
        self.informacoes_frame.configure(bg=color)
        self.informacoes_frame.grid(row=0, column=0, padx=16, pady=16)

        self.label = tk.Label(
            self.informacoes_frame,
            bg=color,
            fg='white',
            text='Tem certeza de que deseja excluir o seguinte favorito?',
            font=('serif', 16)
        )
        self.label.grid(row=0, column=0, padx=16, pady=16)

        self.label = tk.Label(
            self.informacoes_frame,
            bg=color,
            fg='white',
            text=f'Id: {favorito.id}',
            font=('serif', 16)
        )
        self.label.grid(row=1, column=0, padx=16, pady=16)

        self.label = tk.Label(
            self.informacoes_frame,
            bg=color,
            fg='white',
            text=f'Nome: {favorito.nome}',
            font=('serif', 16)
        )
        self.label.grid(row=2, column=0, padx=16, pady=16)

        self.label = tk.Label(
            self.informacoes_frame,
            bg=color,
            fg='white',
            text=f'URL: {favorito.url}',
            font=('serif', 16)
        )
        self.label.grid(row=3, column=0, padx=16, pady=16)

        self.buttons_frame = tk.Frame(self.frame)
        self.buttons_frame.configure(bg=color)
        self.buttons_frame.grid(row=1, column=0, padx=16, pady=16)
        
        self.sim_button = tk.Button(
            self.buttons_frame,
            bg='#BF4040',
            fg='white',
            font=('serif', 16),
            text='Sim',
            command=self.excluir
        )
        self.sim_button.grid(row=0, column=0, padx=16, pady=16)
        
        self.nao_button = tk.Button(
            self.buttons_frame,
            bg='#408040',
            fg='white',
            font=('serif', 16),
            text='Não',
            command=self.desistir
        )
        self.nao_button.grid(row=0, column=1, padx=16, pady=16)

        Ico(self.janela).mostrar()
        self.janela.attributes('-zoomed', True)
        self.janela.mainloop()

    def excluir(self) -> None:
        from controllers.FavoritoController import FavoritoController
        self.janela.destroy()
        FavoritoController().excluir(self.favorito.id)
    
    def desistir(self) -> None:
        from controllers.AssuntoController import AssuntoController
        self.janela.destroy()
        AssuntoController().listar()