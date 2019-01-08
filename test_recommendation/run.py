from text_classifier.algorithm.FitModel import Fit
from text_classifier import database
from text_classifier.create_database import createDatabase
import text_classifier.model as m

def create_table():
    database.create_all()
    database.session.commit()

def insertData(sentences):
    object = None
    for sentence in sentences:
        if area == "biologia":
            object = m.BiologiaModel.Biologia(sentence)
        elif area == "filosofia":
            object = m.FilosofiaModel.Filosofia(sentence)
        elif area == "fisica":
            object = m.FisicaModel.Fisica(sentence)
        elif area == "geografia":
            object = m.GeografiaModel.Geografia(sentence)
        elif area == "historia":
            object = m.HistoriaModel.Historia(sentence)
        elif area == "ingles":
            object = m.InglesModel.Ingles(sentence)
        elif area == "matematica":
            object = m.MatematicaModel.Matematica(sentence)
        elif area == "portugues":
            object = m.PortuguesModel.Portugues(sentence)
        elif area == "quimica":
            object = m.QuimicaModel.Quimica(sentence)
        elif area == "sociologia":
            object = m.SociologiaModel.Sociologia(sentence)
        if object != None:
            database.session.add(object)
    database.session.commit()

def table_exists(name):
    return database.engine.dialect.has_table(database.engine, name)

if __name__ == "__main__":
    while True:
        area = input("Informe a área de conhecimento sem acentos e/ou caracteres especiais (digite 0 para sair): ").lower()
        if area == 0:
            break
        text = input("Digite o texto: ")

        if not table_exists(area):
            createDatabase()

        fitData = Fit()
        if insertData(fitData.split_into_sentences(text)) == None:
            print("Cadastro(s) realizado(s) com sucesso!")