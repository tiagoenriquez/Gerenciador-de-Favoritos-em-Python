from functools import partial
from tkinter import *

from Favorito import Favorito

class InsercaoFrame:

    def inserir(self, nome_entry, url_entry, assunto_entry):
        nome_inserido = nome_entry.get()
        url_inserido = url_entry.get()
        assunto_inserido = assunto_entry.get()
        favorito = Favorito(nome = nome_inserido, url = url_inserido, assunto = assunto_inserido)
        favorito.save()

    def abrir(self):
        janela = Tk()
        janela.title("Inserção de Favoritos")
        janela.geometry("310x260+600+200")
        frame = Frame(janela)
        frame.pack()

        nome_label = Label(janela, width = 10, text = "Nome")
        nome_label.place(x = 20, y = 20)
        nome_entry = Entry(janela, width = 20)
        nome_entry.place(x = 140, y = 20)
        url_label = Label(janela, width = 10, text = "URL")
        url_label.place(x = 20, y = 70)
        url_entry = Entry(janela, width = 20)
        url_entry.place(x = 140, y = 70)
        assunto_label = Label(janela, width = 10, text = "Assunto")
        assunto_label.place(x = 20, y = 120)
        assunto_entry = Entry(janela, width = 20)
        assunto_entry.place(x = 140, y = 120)
        inserir_button = Button(janela, width = 15, text = "Inserir", command = partial(self.inserir, nome_entry, url_entry, assunto_entry))
        inserir_button.place(x = 20, y = 170)

        janela.iconbitmap("favorito.ico")
        janela.mainloop()
