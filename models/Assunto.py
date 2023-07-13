from connection.Connection import Connection
from peewee import *

db = Connection().db()

class Assunto(Model):
    nome = CharField(unique = True)

    class Meta:
        database = db

try:
    db.connect()
    db.create_tables([Assunto])
except Exception as exception:
    raise Exception(exception.args[0])