import os
from datetime import datetime

from peewee import *
from playhouse.db_url import connect



if 'ON_HEROKU' in os.environ:
    DATABASE = PostgresqlDatabase('dern94jbssvdkh', user='zvzvxyydfvrhvm', password='3a2adb4e7583a477af869d4880b2c803fc32e414b489ce6ff1ebb4bc187d8a43',
    host='ec2-54-147-93-73.compute-1.amazonaws.com', port=5432)
else:
    DATABASE = PostgresqlDatabase('dern94jbssvdkh', user='zvzvxyydfvrhvm', password='3a2adb4e7583a477af869d4880b2c803fc32e414b489ce6ff1ebb4bc187d8a43',
    host='ec2-54-147-93-73.compute-1.amazonaws.com', port=5432)

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