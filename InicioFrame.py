from functools import partial
from tkinter import *

from Favorito import Favorito
from FavoritosFrame import FavoritosFrame
from InsercaoFrame import InsercaoFrame

def inserir():
    insercao_frame = InsercaoFrame()
    insercao_frame.abrir()

def escolher_assunto(assunto):
    favoritosFrame = FavoritosFrame()
    favoritosFrame.abrir(assunto)

resultados = Favorito.select(Favorito.assunto).order_by(Favorito.assunto).distinct()
janela = Tk()
janela.title("Gerenciador de Favoritos")
janela.geometry("310x" + str(20 * len(resultados) + 90) + "+600+200")
frame = Frame(janela)
frame.pack()

inserir_button = Button(janela, width = 15, text = "Inserir Favorito", command = inserir)
inserir_button.place(x = 20, y = 20)

assunto_label = Label(janela, width = 15, text = "Escolha um assunto")
assunto_label.place(x = 20, y = 70)

contador = 1
if len(resultados) > 0:
    for resultado in resultados:
        assunto = resultado.assunto
        assunto_button = Button(janela, width = 15, text = assunto, command = partial(escolher_assunto, assunto))
        assunto_button.place(x = 140, y = 20 * contador + 50)
        contador = contador + 1

janela.iconbitmap("favorito.ico")
janela.mainloop()
