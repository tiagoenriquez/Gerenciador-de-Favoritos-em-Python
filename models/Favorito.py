from models.Assunto import Assunto
from connection.Connection import Connection
from peewee import *

db = Connection().db()

class Favorito(Model):
    nome = CharField(unique = True)
    url = CharField()
    assunto = ForeignKeyField(Assunto, backref='favoritos')

    class Meta:
        database = db

try:
    db.connect()
    db.create_tables([Favorito])
except Exception as exception:
    raise Exception(exception.args[0])