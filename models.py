from datetime import datetime

from peewee import *

DATABASE = PostgresqlDatabase('shows')

class Show(Model):
    name = CharField(unique=True)
    type = CharField(unique=True)
    category = CharField(unique=True)
    where = CharField(unique=True)
    created_at = DateTimeField(default=datetime.now)

    class Meta:
        database = DATABASE


def initialize():
    DATABASE.connect()
    DATABASE.create_tables([Show], safe=True)
    print("peewee connected and tables created")
    DATABASE.close()