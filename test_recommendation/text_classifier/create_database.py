from text_classifier import database
from text_classifier.model import BiologiaModel, FilosofiaModel, FisicaModel, GeografiaModel, HistoriaModel, InglesModel\
                                  ,MatematicaModel, PortuguesModel, QuimicaModel, SociologiaModel

def createDatabase():
    BiologiaModel.Biologia
    FilosofiaModel.Filosofia
    FisicaModel.Fisica
    GeografiaModel.Geografia
    HistoriaModel.Historia
    InglesModel.Ingles
    MatematicaModel.Matematica
    PortuguesModel.Portugues
    QuimicaModel.Quimica
    SociologiaModel.Sociologia

    database.create_all()