from models.Assunto import Assunto
from peewee import DoesNotExist

class AssuntoService:

    def inserir(self, nome) -> None:
        try:
            query = Assunto.insert({
                Assunto.nome: nome
            })
            query.execute()
        except Exception as exception:
            raise Exception(f'Impossível inserir assunto: \n{exception}')
    
    def atualizar(self, id, nome) -> None:
        try:
            query = Assunto.update({
                Assunto.nome: nome
            }).where(Assunto.id == id)
            query.execute()
        except Exception as exception:
            raise Exception(f'Impossível atualizar assunto: \n{exception}')
        
    def excluir(self, id):
        try:
            query = Assunto.delete().where(Assunto.id == id)
            query.execute()
        except Exception as exception:
            raise Exception(f'Impossível excluir assunto: \n{exception}')
    
    def procurar(self, id: int) -> Assunto:
        try:
            assunto = Assunto.get_by_id(id)
            return assunto
        except Exception as exception:
            raise Exception(f'Impossível procurar o assunto: \n{exception}')
    
    def procurar_por_nome(self, nome: str) -> Assunto | None:
        try:
            assunto = Assunto.select().where(Assunto.nome == nome).get()
            return assunto
        except DoesNotExist:
            return None
        except Exception as exception:
            mensagem = f'Impossível procurar o assunto por nome: \n{exception}'
            raise Exception(mensagem)
    
    def listar(self) -> list[Assunto]:
        try:
            assuntos = Assunto.select().order_by(Assunto.nome)
            return assuntos
        except Exception as exception:
            raise Exception(f'Impossível listar os assuntos: \n{exception}')