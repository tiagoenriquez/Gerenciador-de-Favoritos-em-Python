from models.Assunto import Assunto
from tkinter import ttk
from views.Ico import Ico
import tkinter as tk

class CriacaoDeFavoritoView:

    def __init__(self, assuntos: list[Assunto]):
        color = '#404040'

        self.janela = tk.Tk()
        self.janela.title('Gerenciador de Favoritos - Criação de Favorito')
        self.janela.configure(bg=color)
        largura_tela = self.janela.winfo_screenwidth()
        altura_tela = self.janela.winfo_screenheight()
        self.janela.geometry(f"{largura_tela}x{altura_tela}+0+0")

        self.frame = tk.Frame(self.janela)
        self.frame.configure(bg=color)
        self.frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.insercao_de_dados_frame = tk.Frame(self.frame)
        self.insercao_de_dados_frame.configure(bg=color)
        self.insercao_de_dados_frame.grid(row=0, column=0, padx=16, pady=16)

        self.nome_label = tk.Label(
            self.insercao_de_dados_frame,
            bg=color,
            fg='white',
            text='Nome do Favorito',
            font=('serif', 16)
        )
        self.nome_label.grid(row=0, column=0, padx=16, pady=16)

        self.nome_entry = tk.Entry(
            self.insercao_de_dados_frame,
            font=('serif', 16)
        )
        self.nome_entry.grid(row=0, column=1, padx=16, pady=16)

        self.url_label = tk.Label(
            self.insercao_de_dados_frame,
            bg=color,
            fg='white',
            text='URL',
            font=('serif', 16)
        )
        self.url_label.grid(row=1, column=0, padx=16, pady=16)

        self.url_entry = tk.Entry(
            self.insercao_de_dados_frame,
            font=('serif', 16)
        )
        self.url_entry.grid(row=1, column=1, padx=16, pady=16)

        self.selecao_de_assunto_label = tk.Label(
            self.insercao_de_dados_frame,
            bg=color,
            fg='white',
            text='Selecione um assunto',
            font=('serif', 16)
        )
        self.selecao_de_assunto_label.grid(row=2, column=0, padx=16, pady=16)

        fonte = ('serif', 16)
        style = ttk.Style()
        style.configure(
            'style.TCombobox',
            font=fonte,
            background=color,
            foreground='white',
            padding=(16, 8)
        )
        self.nome_dos_assuntos = [(assunto.nome) for assunto in assuntos]
        self.combo = ttk.Combobox(
            self.insercao_de_dados_frame,
            values=self.nome_dos_assuntos,
            style='style.TCombobox'
        )
        self.combo.grid(row=2, column=1, padx=16, pady=16)
        self.combo.bind(
            '<<ComboboxSelected>>',
            lambda event: self.escolher_assunto()
        )

        self.novo_assunto_label = tk.Label(
            self.insercao_de_dados_frame,
            bg=color,
            fg='white',
            text='Digite um assunto',
            font=('serif', 16)
        )
        self.novo_assunto_label.grid(row=3, column=0, padx=16, pady=16)

        self.assunto_entry = tk.Entry(
            self.insercao_de_dados_frame,
            font=('serif', 16)
        )
        self.assunto_entry.grid(row=3, column=1, padx=16, pady=16)

        self.button_frame = tk.Frame(self.frame)
        self.button_frame.configure(bg=color)
        self.button_frame.grid(row=1, column=0, padx=16, pady=16)
        
        self.inserir_button = tk.Button(
            self.button_frame,
            bg=color,
            fg='white',
            font=('serif', 16),
            text='Inserir Favorito',
            command=self.inserir
        )
        self.inserir_button.grid(row=0, column=4, padx=16, pady=16)

        Ico(self.janela).mostrar()
        self.janela.attributes('-zoomed', True)
        self.janela.mainloop()

    def escolher_assunto(self) -> None:
        assuntoEscolhido = self.combo.get()
        self.assunto_entry.delete(0, tk.END)
        self.assunto_entry.insert(tk.END, assuntoEscolhido)
    
    def inserir(self) -> None:
        nome = self.nome_entry.get()
        url = self.url_entry.get()
        assunto = self.assunto_entry.get()
        from controllers.FavoritoController import FavoritoController
        self.janela.destroy()
        FavoritoController().inserir(nome, url, assunto)