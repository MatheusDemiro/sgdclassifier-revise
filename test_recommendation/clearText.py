from sklearn.decomposition import NMF, LatentDirichletAllocation, TruncatedSVD
from sklearn.linear_model import SGDClassifier
from sklearn.pipeline import Pipeline
from stop_words import get_stop_words
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.datasets import fetch_20newsgroups
from sklearn.datasets import fetch_rcv1
from sklearn.naive_bayes import MultinomialNB

twenty_train = fetch_20newsgroups(subset='train', shuffle=True)
# rcv1 = fetch_rcv1()
#
# print(rcv1.target_names)
print(twenty_train.target_names)

count_vect = CountVectorizer ()
tfidf_transformer = TfidfTransformer()

X_train_counts = count_vect.fit_transform(twenty_train.data)
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)

clf = MultinomialNB().fit(X_train_tfidf, twenty_train.target)

text_clf = Pipeline([('vect', CountVectorizer(stop_words='english')),
                    ('tfidf', TfidfTransformer()),
                    ('clf', SGDClassifier(loss='log', penalty='l2', alpha=1e-3, max_iter=5, random_state=42))])

text_clf = text_clf.fit(twenty_train.data, twenty_train.target)

twenty_test = fetch_20newsgroups(subset='test', shuffle=True)
predicted = text_clf.predict(["Powerful vehicle with 10 horsepower"])

#print(twenty_test)
#print(count_vect.vocabulary_)
print(predicted)
print(twenty_test.target_names[predicted[0]])
print(np.mean(predicted == twenty_test.target))


# NUM_TOPICS = 10
#
# corpus = [
#     "A matemática é a ciência do raciocínio lógico e abstrato, que estuda quantidades, medidas, espaços, estruturas, variações e estatísticas. ",
#     'derivada',
#     'limite derivada',
#     'derivada limite'
# ]
#
# vectorizer = CountVectorizer(stop_words=get_stop_words("portuguese"))
# data_vectorized = vectorizer.fit_transform(corpus)
# print(vectorizer.vocabulary_)
# print(vectorizer.get_feature_names())
# print(data_vectorized.toarray())
#
# # Build a Latent Dirichlet Allocation Model
# lda_model = LatentDirichletAllocation(n_components=NUM_TOPICS, learning_method='online')
# lda_Z = lda_model.fit_transform(data_vectorized)
# print(lda_Z.shape)  # (NO_DOCUMENTS, NO_TOPICS)
#
#
# def print_topics(model, vectorizer, top_n=10):
#     for idx, topic in enumerate(model.components_):
#         print("Topic %d:" % (idx))
#         print([(vectorizer.get_feature_names()[i], topic[i])
#                for i in topic.argsort()[:-top_n - 1:-1]])
#
# print("LDA Model:")
# print_topics(lda_model, vectorizer)
# print("=" * 20)

# # Build a Non-Negative Matrix Factorization Model
# nmf_model = NMF(n_components=NUM_TOPICS)
# nmf_Z = nmf_model.fit_transform(data_vectorized)
#print(nmf_Z.shape)  # (NO_DOCUMENTS, NO_TOPICS)

# # Build a Latent Semantic Indexing Model
# lsi_model = TruncatedSVD(n_components=NUM_TOPICS)
# lsi_Z = lsi_model.fit_transform(data_vectorized)
# print(lsi_Z.shape)  # (NO_DOCUMENTS, NO_TOPICS)

# Let's see how the first document in the corpus looks like in different topic spaces
#print(lda_Z[0])
#print(nmf_Z[0])
# print(lsi_Z[0])