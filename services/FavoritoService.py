from services.AssuntoService import AssuntoService
from models.Favorito import Favorito
import webbrowser

class FavoritoService:

    def inserir(self, nome: str, url: str, nome_assunto: int) -> None:
        try: 
            assunto = None
            while assunto == None:
                assunto = AssuntoService().procurar_por_nome(nome_assunto)
                if assunto == None:
                    AssuntoService().inserir(nome_assunto)
            query = Favorito.insert({
                Favorito.nome: nome,
                Favorito.url: url,
                Favorito.assunto: assunto.id
            })
            query.execute()
        except Exception as exception:
            raise Exception(f'Impossível inserir favorito: \n{exception}')
    
    def atualizar(self, id, nome: str, url: str, nome_assunto: str) -> None:
        try: 
            assunto = None
            while assunto == None:
                assunto = AssuntoService().procurar_por_nome(nome_assunto)
                if assunto == None:
                    AssuntoService().inserir(nome_assunto)
            favorito = self.procurar(id)
            query = Favorito.update({
                Favorito.nome: nome,
                Favorito.url: url,
                Favorito.assunto: assunto.id
            }).where(Favorito.id == id)
            query.execute()
            self.excluir_assunto(favorito)
        except Exception as exception:
            raise Exception(f'Impossível atualizar favorito: \n{exception}')
    
    def excluir(self, id):
        try:
            favorito = self.procurar(id)
            query = Favorito.delete().where(Favorito.id == id)
            query.execute()
            self.excluir_assunto(favorito)
        except Exception as exception:
            raise Exception(f'Impossível excluir favorito: \n{exception}')
    
    def procurar(self, id: int) -> Favorito:
        try:
            favorito = Favorito.get_by_id(id)
            return favorito
        except Exception as exception:
            raise Exception(f'Impossível procurar o favorito: \n{exception}')
    
    def listar(self, assunto: str) -> list[Favorito]:
        try:
            idAssunto = AssuntoService().procurar_por_nome(assunto).id
            favoritos = Favorito.select().where(
                Favorito.assunto == idAssunto).order_by(Favorito.nome)
            return favoritos
        except Exception as exception:
            raise Exception(f'Impossível listar os favoritos: \n{exception}')
    
    def excluir_assunto(self, favorito: Favorito) -> None:
        try:
            idAssunto = favorito.assunto
            assunto = AssuntoService().procurar(idAssunto)
            qtd_favoritos_do_assunto = self.listar(assunto.nome).count()
            if qtd_favoritos_do_assunto == 0:
                AssuntoService().excluir(assunto)
        except Exception as exception:
            raise Exception(f'Impossível listar os favoritos: \n{exception}')
    
    def abrir(self, id: int) -> None:
        try:
            favorito = self.procurar(id)
            webbrowser.open(favorito.url)
        except Exception as exception:
            raise Exception(f'Impossível listar os favoritos: \n{exception}')
    
    def pesquisar_conteudo_no_site(self, id: int, conteudo: str) -> None:
        try:
            favorito = self.procurar(id)
            url = 'https://www.google.com/search?q='
            url += f'{conteudo}'
            url += '+site%3A'
            url += favorito.url
            webbrowser.open(url)
        except Exception as exception:
            raise Exception(f'Impossível listar os favoritos: \n{exception}')