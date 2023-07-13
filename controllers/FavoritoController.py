from controllers.AssuntoController import AssuntoController
from services.AssuntoService import AssuntoService
from services.FavoritoService import FavoritoService
from views.CriacaoDeFavoritoView import CriacaoDeFavoritoView
from views.EdicaoDeFavoritoView import EdicaoDeFavoritoView
from views.ErroView import ErroView
from views.ExclusaoDeFavoritoView import ExclusaoDeFavoritoView
from views.FavoritosView import FavoritosView

class FavoritoController:
    
    def listar(self, assunto: str) -> None:
        try:
            favoritos = FavoritoService().listar(assunto)
            FavoritosView(favoritos, assunto)
        except Exception as exception:
            ErroView(exception)

    def criar(self) -> None:
        assuntos = AssuntoService().listar()
        CriacaoDeFavoritoView(assuntos)
    
    def inserir(self, nome: str, url: str, assunto: str) -> None:
        try:
            FavoritoService().inserir(nome, url, assunto)
            AssuntoController().listar()
        except Exception as exception:
            ErroView(exception)
    
    def editar(self, id: int):
        try:
            favorito = FavoritoService().procurar(id)
            assunto = AssuntoService().procurar(favorito.assunto)
            assuntos = AssuntoService().listar()
            EdicaoDeFavoritoView(favorito, assunto, assuntos)
        except Exception as exception:
            ErroView(exception)
    
    def atualizar(self, id: int, nome: str, url: str, assunto: str) -> None:
        try:
            FavoritoService().atualizar(id, nome, url, assunto)
            self.listar(assunto)
        except Exception as exception:
            ErroView(exception)
    
    def ameacar(self, id) -> None:
        try:
            favorito = FavoritoService().procurar(id)
            ExclusaoDeFavoritoView(favorito)
        except Exception as exception:
            ErroView(exception)
    
    def excluir(self, id: int) -> None:
        try:
            FavoritoService().excluir(id)
            AssuntoController().listar()
        except Exception as exception:
            ErroView(exception)
    
    def abrir(self, id: int) -> None:
        try:
            FavoritoService().abrir(id)
        except Exception as exception:
            ErroView(exception)
    
    def pesquisar_no_google(self, id: int, conteudo: str) -> None:
        try:
            FavoritoService().pesquisar_conteudo_no_site(id, conteudo)
        except Exception as exception:
            ErroView(exception)