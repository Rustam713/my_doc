
from peewee import *


db = SqliteDatabase('user.db')


class User(Model):
    id = PrimaryKeyField(unique=True)
    name = CharField(
        max_length=222,
        null=True,
        index=True,
        unique=True,
        #column_name='names',
        default='пусто',
        help_text='сюда впиши имя',
        verbose_name='имена'
    )

    NICK = [
        (1, 'q'),
        (1, 'w'),
        (1, 'e'),
        (1, 'r'),
        (1, 't')
    ]

    nickname = CharField(
        max_length=20,
        choices=NICK

    )






