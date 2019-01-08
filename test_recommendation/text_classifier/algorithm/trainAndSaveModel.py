from sklearn.linear_model import SGDClassifier
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import (TfidfTransformer, CountVectorizer)
from sklearn.model_selection import GridSearchCV
from stop_words import get_stop_words

from text_classifier.controller import SentenceController as sc
import pickle as p

biologia, filosofia, fisica, geografia, historia, ingles, matematica, portugues, quimica, sociologia = sc.getAllSentences()

#X -> features, y -> label
sentences = portugues
subjects = ['portugues'] * portugues[-1].id

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
        gs_clf_svm = gs_clf_svm.fit(sentences, subjects)
        with open('text_classifier\\algorithm\\my_dumped_classifier.pkl', 'wb') as fid:
            gnb_loaded = p.dump(gs_clf_svm, fid)