from functools import partial
from tkinter import *
import webbrowser

from CorrecaoFrame import CorrecaoFrame
from Favorito import Favorito

class FavoritosFrame:

    def abrir_site(self, url):
        webbrowser.open(url)

    def pesquisar(self, url_pesquisada, pesquisa_entry):
        pesquisa = pesquisa_entry.get()
        url = "https://www.google.com/search?q=" + pesquisa + " site:" + url_pesquisada
        webbrowser.open(url)

    def corrigir(self, favorito):
        correcao_frame = CorrecaoFrame()
        correcao_frame.abrir(favorito)

    def remover(self, id):
        query = Favorito.delete().where(Favorito.id == id)
        query.execute()

    def abrir(self, assunto):
        favoritos = Favorito.select().order_by(Favorito.nome).where(Favorito.assunto == assunto)
        janela = Tk()
        janela.title("Lista de Favoritos")
        janela.geometry("1160x" + str(30 * len(favoritos) + 60) + "+200+200")
        frame = Frame(janela)
        frame.pack()
        
        id_label = Label(janela, width = 10, text = "Id", background = "#BFBFBF")
        id_label.place(x = 20, y = 20)
        nome_label = Label(janela, width = 20, text = "Favorito", background = "#BFBFBF")
        nome_label.place(x = 120, y = 20)
        url_label = Label(janela, width = 40, text = "Url", background = "#BFBFBF")
        url_label.place(x = 300, y = 20)

        contador = 1
        for favorito in favoritos:
            id_label = Label(janela, width = 10, text = favorito.id, background = "white")
            id_label.place(x = 20, y = 30 * contador + 20)
            nome_label = Label(janela, width = 20, text = favorito.nome, background = "white")
            nome_label.place(x = 120, y = 30 * contador + 20)
            url_label = Label(janela, width = 40, text = favorito.url, background = "white")
            url_label.place(x = 300, y = 30 * contador + 20)
            abrir_site_button = Button(janela, width = 10, text = "Abrir site", command = partial(self.abrir_site, favorito.url))
            abrir_site_button.place(x = 610, y = 30 * contador + 20)
            pesquisa_entry = Entry(janela, width = 20)
            pesquisa_entry.place(x = 710, y = 30 * contador + 20)
            pesquisar_button = Button(janela, width = 10, text = "Pesquisar", command = partial(self.pesquisar, favorito.url, pesquisa_entry))
            pesquisar_button.place(x = 850, y = 30 * contador + 20)
            corrigir_button = Button(janela, width = 10, text = "Corrigir", command = partial(self.corrigir, favorito))
            corrigir_button.place(x = 950, y = 30 * contador + 20)
            remover_button = Button(janela, width = 10, text = "Remover", command = partial(self.remover, favorito.id))
            remover_button.place(x = 1050, y = 30 * contador + 20)
            contador = contador + 1

        janela.iconbitmap("favorito.ico")
        janela.mainloop()
