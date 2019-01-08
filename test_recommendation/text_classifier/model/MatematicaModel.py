from text_classifier import database
from marshmallow import Schema, fields

class Matematica(database.Model):
    __tablename__ = "matematica"

    id = database.Column(database.Integer, primary_key=True)
    text = database.Column(database.String(2000), nullable=False)

    def __init__(self, text):
        self.text = text

class MatematicaSchema(Schema):
    text = fields.String(many=True)