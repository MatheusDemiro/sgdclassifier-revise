from text_classifier.model import BiologiaModel, FilosofiaModel, FisicaModel, GeografiaModel, HistoriaModel, InglesModel\
                                  ,MatematicaModel, PortuguesModel, QuimicaModel, SociologiaModel

def getAllSentences():
    biologia = ('biologia', BiologiaModel.Biologia.query.all())
    filosofia = ('filosofia' ,FilosofiaModel.Filosofia.query.all())
    fisica = ('fisica' ,FisicaModel.Fisica.query.all())
    geografia = ('geografia' ,GeografiaModel.Geografia.query.all())
    historia = ('historia' ,HistoriaModel.Historia.query.all())
    ingles = ('ingles' ,BiologiaModel.Biologia.query.all())
    matematica = ('matematica' ,MatematicaModel.Matematica.query.all())
    portugues = ('portugues' ,PortuguesModel.Portugues.query.all())
    quimica = ('quimica' ,QuimicaModel.Quimica.query.all())
    sociologia = ('sociologia',SociologiaModel.Sociologia.query.all())

    return [biologia, filosofia, fisica, geografia, historia, ingles, matematica, portugues, quimica, sociologia]