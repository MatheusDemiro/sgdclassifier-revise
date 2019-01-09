from sklearn.linear_model import SGDClassifier
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import (TfidfTransformer, CountVectorizer)
from sklearn.model_selection import GridSearchCV
from stop_words import get_stop_words

from text_classifier.controller import SentenceController as sc
import pickle as p

tablesList = sc.getAllSentences()
#X -> features, y -> label
sentences = []
subjects = []

for table in tablesList:
    sentences+=[i.text for i in table[1]]
    #print(table[0])
    #print(table[1][-1].id)
    subjects+=[table[0] for i in range(table[1][-1].id)]

text_clf_svm = Pipeline([('vect', CountVectorizer(stop_words=get_stop_words("portuguese"))),
                         ('tfidf', TfidfTransformer()),
                         ('clf', SGDClassifier(loss='log', penalty='l2', alpha=1e-3, max_iter=5, random_state=42))
                         ])
#Parametros
parameters = {'vect__ngram_range': [(1, 1), (1, 2)],
              'tfidf__use_idf': (True, False),
              'clf__alpha': (1e-2, 1e-3),
              }
#Training a linear SVM classifier
if __name__ == '__main__':
        gs_clf_svm = GridSearchCV(text_clf_svm, parameters, n_jobs=-1)
        print(sentences)
        print(subjects)
        gs_clf_svm = gs_clf_svm.fit(sentences, subjects)
        with open('my_dumped_classifier.pkl', 'wb') as fid:
            gnb_loaded = p.dump(gs_clf_svm, fid)
        with open('my_dumped_classifier.pkl', 'rb') as fid:
            gnb_loaded = p.load(fid)
        while True:
            pergunta = input()
            print('Pergunta: %s\nResposta: %s'%(pergunta,gnb_loaded.predict([pergunta])[0]))
        #('Pergunta: Quero saber de história\n',gnb_loaded.predict(['derivada da velocidade?']))