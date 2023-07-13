from functools import partial
from models.Favorito import Favorito
from views.Ico import Ico
import tkinter as tk

class FavoritosView:

    def __init__(self, favoritos: list[Favorito], assunto: str) -> None:
        self.favoritos = favoritos
        color = '#404040'

        self.janela = tk.Tk()
        self.janela.title(f'Gerenciador de Favoritos - {assunto}')
        self.janela.configure(bg=color)
        largura_tela = self.janela.winfo_screenwidth()
        altura_tela = self.janela.winfo_screenheight()
        self.janela.geometry(f"{largura_tela}x{altura_tela}+0+0")

        self.frame = tk.Frame(self.janela)
        self.frame.configure(bg=color)
        self.frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.favoritos_frame = tk.Frame(self.frame)
        self.favoritos_frame.configure(bg=color)
        self.favoritos_frame.grid(row=0, column=0, padx=16, pady=16)

        for n in range(len(favoritos)):
            id = favoritos[n].id
            nome = favoritos[n].nome
            
            self.nome_label = tk.Label(
                self.favoritos_frame,
                bg=color,
                fg='white',
                text=str(nome),
                font=('serif', 16)
            )
            self.nome_label.grid(row=n, column=0, padx=16, pady=16)

            self.texto_a_ser_pesquisado_entry = tk.Entry(
                self.favoritos_frame,
                font=('serif', 16)
            )
            self.texto_a_ser_pesquisado_entry.insert(0, f'Pesquise em {nome}')
            self.texto_a_ser_pesquisado_entry.grid(
                row=n,
                column=1,
                padx=16,
                pady=16
            )
        
            self.abrir_button = tk.Button(
                self.favoritos_frame,
                bg=color,
                fg='white',
                font=('serif', 16),
                text='Abrir',
                command=partial(self.abrir, id)
            )
            self.abrir_button.grid(row=n, column=2, padx=16, pady=16)
        
            self.pesquisar_button = tk.Button(
                self.favoritos_frame,
                bg=color,
                fg='white',
                font=('serif', 16),
                text='Pesquisar',
                command=partial(
                    self.pesquisar,
                    id,
                    self.texto_a_ser_pesquisado_entry
                )
            )
            self.pesquisar_button.grid(row=n, column=3, padx=16, pady=16)
        
            self.corrigir_button = tk.Button(
                self.favoritos_frame,
                bg=color,
                fg='white',
                font=('serif', 16),
                text='Corrigir',
                command=partial(self.corrigir, id)
            )
            self.corrigir_button.grid(row=n, column=4, padx=16, pady=16)
        
            self.excluir_button = tk.Button(
                self.favoritos_frame,
                bg=color,
                fg='white',
                font=('serif', 16),
                text='Excluir',
                command=partial(self.excluir, id)
            )
            self.excluir_button.grid(row=n, column=5, padx=16, pady=16)

        self.assuntos_button_frame = tk.Frame(self.frame)
        self.assuntos_button_frame.configure(bg=color)
        self.assuntos_button_frame.grid(row=1, column=0, padx=16, pady=16)

        self.assuntos_button = tk.Button(
            self.assuntos_button_frame,
            bg=color,
            fg='white',
            font=('serif', 16),
            text='Listar Assuntos',
            command=self.listar_assuntos
        )
        self.assuntos_button.grid(row=0, column=0, padx=16, pady=16)

        Ico(self.janela).mostrar()
        self.janela.attributes('-zoomed', True)
        self.janela.mainloop()
    
    def abrir(self, id: int) -> None:
        from controllers.FavoritoController import FavoritoController
        FavoritoController().abrir(id)
    
    def pesquisar(self, id: int, entry: tk.Entry) -> None:
        texto = entry.get()
        from controllers.FavoritoController import FavoritoController
        FavoritoController().pesquisar_no_google(id, texto)
    
    def corrigir(self, id: int) -> None:
        from controllers.FavoritoController import FavoritoController
        self.janela.destroy()
        FavoritoController().editar(id)
    
    def excluir(self, id: int) -> None:
        from controllers.FavoritoController import FavoritoController
        self.janela.destroy()
        FavoritoController().ameacar(id)
    
    def listar_assuntos(self) -> None:
        from controllers.AssuntoController import AssuntoController
        self.janela.destroy()
        AssuntoController().listar()