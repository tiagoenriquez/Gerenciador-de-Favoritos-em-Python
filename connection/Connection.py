from peewee import *
import os

class Connection:
    
    def db(self):
        try:
            if os.path.exists('sql_databases'):
                return SqliteDatabase(
                    'sql_databases/gerenciamento_de_favoritos.db'
                )
            else:
                return SqliteDatabase('gerenciamento_de_favoritos.db')
        except Exception as e:
            raise Exception(f'Erro na conexão com banco de dados.\n{e}')