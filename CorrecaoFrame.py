from functools import partial
from tkinter import *

from Favorito import Favorito

class CorrecaoFrame:

    def corrigir(self, id, nome_entry, url_entry, assunto_entry):
        nome_correto = nome_entry.get()
        url_correto = url_entry.get()
        assunto_correto = assunto_entry.get()
        query = Favorito.update({Favorito.nome: nome_correto, Favorito.url: url_correto, Favorito.assunto: assunto_correto}).where(Favorito.id == id)
        query.execute()

    def abrir(self, favorito):
        janela = Tk()
        janela.title("Correção de Favorito")
        janela.geometry("410x260+600+200")
        frame = Frame(janela)
        frame.pack()
        
        nome_label = Label(janela, width = 10, text = "Nome")
        nome_label.place(x = 20, y = 20)
        nome_entry = Entry(janela, width = 20, text = favorito.nome)
        nome_entry.place(x = 140, y = 20)
        nome_entry.insert(0, favorito.nome)
        
        url_label = Label(janela, width = 10, text = "URL")
        url_label.place(x = 20, y = 70)
        url_entry = Entry(janela, width = 20, text = favorito.url)
        url_entry.place(x = 140, y = 70)
        url_entry.insert(0, favorito.url)
        
        assunto_label = Label(janela, width = 10, text = "Assunto")
        assunto_label.place(x = 20, y = 120)
        assunto_entry = Entry(janela, width = 20, text = favorito.assunto)
        assunto_entry.place(x = 140, y = 120)
        assunto_entry.insert(0, favorito.assunto)
        
        inserir_button = Button(janela, width = 15, text = "Corrigir", command = partial(self.corrigir, favorito.id, nome_entry, url_entry, assunto_entry))
        inserir_button.place(x = 20, y = 170)

        janela.iconbitmap("favorito.ico")
        janela.mainloop()
