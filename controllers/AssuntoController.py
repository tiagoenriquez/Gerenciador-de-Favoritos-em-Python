from services.AssuntoService import AssuntoService
from views.AssuntosView import AssuntosView
from views.EdicaoDeAssuntoView import EdicaoDeAssuntoView
from views.ErroView import ErroView

class AssuntoController:

    def listar(self) -> None:
        try:
            assuntos = AssuntoService().listar()
            AssuntosView(assuntos)
        except Exception as exception:
            ErroView(exception)
    
    def editar(self, nome: str) -> None:
        try:
            assunto = AssuntoService().procurar_por_nome(nome)
            EdicaoDeAssuntoView(assunto)
        except Exception as exception:
            ErroView(exception)
    
    def atualizar(self, id: int, nome: str) -> None:
        try:
            AssuntoService().atualizar(id, nome)
            self.listar()
        except Exception as exception:
            ErroView(exception)