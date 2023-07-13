import tkinter as tk

class Ico:

    def __init__(self, janela: tk):
        self.janela = janela
        self.ICONE = 'favorito.ico'
    
    def mostrar(self) -> None:
        try:
            self.janela.iconbitmap(self.ICONE)
        except:
            pass