import os
from datetime import datetime

from peewee import *
from playhouse.db_url import connect



if 'ON_HEROKU' in os.environ:
    DATABASE = connect(os.environ.get('https://next-flick.herokuapp.com/'))
else:
    DATABASE = PostgresqlDatabase('shows')

class Show(Model):
    name = CharField(unique=True)
    type = CharField()
    category = CharField()
    where = CharField()
    created_at = DateTimeField(default=datetime.now)

    class Meta:
        database = DATABASE


def initialize():
    DATABASE.connect()
    DATABASE.create_tables([Show], safe=True)
    print("peewee connected and tables created")
    DATABASE.close()