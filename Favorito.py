from peewee import *

db = SqliteDatabase("gerenciamento_de_favoritos.db")

class Favorito(Model):
    nome = CharField(unique = True)
    url = CharField()
    assunto = CharField()

    class Meta:
        database = db

db.connect()
db.create_tables([Favorito])
