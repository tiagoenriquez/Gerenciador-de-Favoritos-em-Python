from models.Assunto import Assunto
from models.Favorito import Favorito
from tkinter import ttk
from views.Ico import Ico
import tkinter as tk
class EdicaoDeFavoritoView:

    def __init__(
            self,
            favorito: Favorito,
            assunto: Assunto,
            assuntos: list[Assunto]
    ):
        self.favorito = favorito
        color = '#404040'

        self.janela = tk.Tk()
        self.janela.title('Gerenciador de Favoritos - Edição de Favorito')
        self.janela.configure(bg=color)
        largura_tela = self.janela.winfo_screenwidth()
        altura_tela = self.janela.winfo_screenheight()
        self.janela.geometry(f"{largura_tela}x{altura_tela}+0+0")

        self.frame = tk.Frame(self.janela)
        self.frame.configure(bg=color)
        self.frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.inserir_dados_frame = tk.Frame(self.frame)
        self.inserir_dados_frame.configure(bg=color)
        self.inserir_dados_frame.grid(row=0, column=0, padx=16, pady=16)

        self.id_label = tk.Label(
            self.inserir_dados_frame,
            bg=color,
            fg='white',
            text='Id',
            font=('serif', 16)
        )
        self.id_label.grid(row=1, column=0, padx=16, pady=16)

        self.id_entry = tk.Label(
            self.inserir_dados_frame,
            bg=color,
            fg='white',
            text=favorito.id,
            font=('serif', 16)
        )
        self.id_entry.grid(row=1, column=0, padx=16, pady=16)

        self.nome_label = tk.Label(
            self.inserir_dados_frame,
            bg=color,
            fg='white',
            text='Nome do Favorito',
            font=('serif', 16)
        )
        self.nome_label.grid(row=1, column=0, padx=16, pady=16)

        self.nome_entry = tk.Entry(
            self.inserir_dados_frame,
            font=('serif', 16)
        )
        self.nome_entry.insert(0, favorito.nome)
        self.nome_entry.grid(row=1, column=1, padx=16, pady=16)

        self.url_label = tk.Label(
            self.inserir_dados_frame,
            bg=color,
            fg='white',
            text='URL',
            font=('serif', 16)
        )
        self.url_label.grid(row=2, column=0, padx=16, pady=16)

        self.url_entry = tk.Entry(
            self.inserir_dados_frame,
            font=('serif', 16)
        )
        self.url_entry.insert(0, favorito.url)
        self.url_entry.grid(row=2, column=1, padx=16, pady=16)

        self.selecionar_assunto_label = tk.Label(
            self.inserir_dados_frame,
            bg=color,
            fg='white',
            text='Selecione um assunto',
            font=('serif', 16)
        )
        self.selecionar_assunto_label.grid(row=3, column=0, padx=16, pady=16)

        fonte = ('serif', 16)
        style = ttk.Style()
        style.configure(
            'style.TCombobox',
            font=fonte,
            background=color,
            foreground='white',
            padding=(16, 8)
        )
        self.nomes_dos_assuntos = [(assunto.nome) for assunto in assuntos]
        self.combo = ttk.Combobox(
            self.inserir_dados_frame,
            values=self.nomes_dos_assuntos,
            style='style.TCombobox'
        )
        self.combo.grid(row=3, column=1, padx=16, pady=16)
        self.combo.bind(
            '<<ComboboxSelected>>',
            lambda event: self.escolher_assunto()
        )

        self.novo_assunto_label = tk.Label(
            self.inserir_dados_frame,
            bg=color,
            fg='white',
            text='Digite um assunto',
            font=('serif', 16)
        )
        self.novo_assunto_label.grid(row=4, column=0, padx=16, pady=16)

        self.assunto_entry = tk.Entry(
            self.inserir_dados_frame,
            font=('serif', 16)
        )
        self.assunto_entry.insert(0, assunto.nome)
        self.assunto_entry.grid(row=4, column=1, padx=16, pady=16)

        self.button_frame = tk.Frame(self.frame)
        self.button_frame.configure(bg=color)
        self.button_frame.grid(row=1, column=0, padx=16, pady=16)
        
        self.atualizar_button = tk.Button(
            self.button_frame,
            bg=color,
            fg='white',
            font=('serif', 16),
            text='Corrigir Favorito',
            command=self.atualizar
        )
        self.atualizar_button.grid(row=0, column=4, padx=16, pady=16)

        Ico(self.janela).mostrar()
        self.janela.attributes('-zoomed', True)
        self.janela.mainloop()

    def escolher_assunto(self) -> None:
        assunto_escolhido = self.combo.get()
        self.assunto_entry.delete(0, tk.END)
        self.assunto_entry.insert(tk.END, assunto_escolhido)

    def atualizar(self) -> None:
        id = self.favorito.id
        nome = self.nome_entry.get()
        url = self.url_entry.get()
        assunto = self.assunto_entry.get()
        from controllers.FavoritoController import FavoritoController
        self.janela.destroy()
        FavoritoController().atualizar(id, nome, url, assunto)