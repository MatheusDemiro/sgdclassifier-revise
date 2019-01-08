from text_classifier import database
from marshmallow import Schema, fields

class Fisica(database.Model):
    __tablename__ = "fisica"

    id = database.Column(database.Integer, primary_key=True)
    text = database.Column(database.String(2000), nullable=False)

    def __init__(self, text):
        self.text = text

class FisicaSchema(Schema):
    text = fields.String(many=True)