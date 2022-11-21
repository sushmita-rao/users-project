from mongoengine import Document, StringField, IntField


class Users(Document):
    name = StringField(),
    number = IntField(),
    password = StringField()
