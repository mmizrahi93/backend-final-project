import os
from datetime import datetime

from peewee import *
from playhouse.db_url import connect



if 'ON_HEROKU' in os.environ:
    DATABASE = connect(os.environ.get('postgres://zvzvxyydfvrhvm:3a2adb4e7583a477af869d4880b2c803fc32e414b489ce6ff1ebb4bc187d8a43@ec2-54-147-93-73.compute-1.amazonaws.com:5432/dern94jbssvdkh'))
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