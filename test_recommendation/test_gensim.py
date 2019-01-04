import re
from gensim import models, corpora
import nltk
from nltk import word_tokenize
from stop_words import get_stop_words

nltk.download('punkt')

NUM_TOPICS = 5
STOPWORDS = get_stop_words('portuguese')

data = ['tenho dúvida de matemática', 'meu nome eh matheus', 'quero cafe']

def clean_text(text):
    tokenized_text = word_tokenize(text.lower())
    cleaned_text = [t for t in tokenized_text if t not in STOPWORDS and re.match('[a-zA-Z\-][a-zA-Z\-]{2,}', t)]
    return cleaned_text

# For gensim we need to tokenize the data and filter out stopwords
tokenized_data = []
for text in data:
    tokenized_data.append(clean_text(text))

# Build a Dictionary - association word to numeric id
dictionary = corpora.Dictionary(tokenized_data)

# Transform the collection of texts to a numerical form
corpus = [dictionary.doc2bow(text) for text in tokenized_data]

# Have a look at how the 20th document looks like: [(word_id, count), ...]
print(corpus)
print(dictionary)
print(tokenized_data)

# Build the LDA model
lda_model = models.LdaModel(corpus=corpus, num_topics=NUM_TOPICS, id2word=dictionary)
for i in range(NUM_TOPICS):
    print(lda_model.show_topic(i))

print("LDA Model:")

for idx in range(NUM_TOPICS):
    # Print the first 10 most representative topics
    print("Topic #%s:" % idx, lda_model.print_topic(idx, 10))

print("=" * 20)

# text = "cafe"
# bow = dictionary.doc2bow(clean_text(text))
#
# print(lda_model[bow])

# Build the LSI model
lsi_model = models.LsiModel(corpus=corpus, num_topics=NUM_TOPICS, id2word=dictionary)