from text_classifier.model import BiologiaModel, FilosofiaModel, FisicaModel, GeografiaModel, HistoriaModel, InglesModel\
                                  ,MatematicaModel, PortuguesModel, QuimicaModel, SociologiaModel

def getAllSentences():
    biologia = BiologiaModel.Biologia.query.all()
    filosofia = FilosofiaModel.Filosofia.query.all()
    fisica = FisicaModel.Fisica.query.all()
    geografia = GeografiaModel.Geografia.query.all()
    historia = HistoriaModel.Historia.query.all()
    ingles = BiologiaModel.Biologia.query.all()
    matematica = MatematicaModel.Matematica.query.all()
    portugues = PortuguesModel.Portugues.query.all()
    quimica = QuimicaModel.Quimica.query.all()
    sociologia = SociologiaModel.Sociologia.query.all()

    return biologia, filosofia, fisica, geografia, historia, ingles, matematica, portugues, quimica, sociologia