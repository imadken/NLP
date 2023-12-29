from gensim import models
from gensim import corpora
import gensim
import nltk
from tqdm import tqdm
from nltk.corpus import reuters
import spacy
nlp = spacy.load("en_core_web_sm")
# nltk.download('reuters')


def accept_token(token):
    return bool(not token.is_stop and not token.is_punct and token.text != " " and not w.like_num)


# List all file IDs in the Reuters Corpus
file_ids = reuters.fileids()
file_content = reuters.sents()

texts = []
documents = [' '.join(doc) for doc in file_content]
documents = documents[:10000]
for document in tqdm(documents):
    text = []
    doc = nlp(document)
    for w in doc:
        if accept_token(w):
            text.append(w.lemma_)
    texts.append(text)

print(texts[:4])
print("="*50)

dictionary = corpora.Dictionary(texts)
# print(dictionary.token2id)

print("="*50)

corpus = [dictionary.doc2bow(text) for text in texts]
print(corpus[:4])

print("="*50)


tfidf = models.TfidfModel(corpus)
tfidf_doc = []
for document in tfidf[corpus]:
    tfidf_doc.append(document)

print(tfidf_doc[:4])
print("="*50)

bigram = gensim.models.Phrases(texts)
bi_grams = [bigram[line] for line in texts]
trigram = gensim.models.Phrases(bi_grams)
tri_grams = [trigram[line] for line in bi_grams]

max_prints = 10

for sentence, bi_gram, tri_gram in zip(texts, bi_grams, tri_grams):
    if bi_gram != sentence:
        print("Original Sentence:", sentence)
        print("Bi-grams:", bi_gram)
        if bi_gram != tri_gram:
            print("Tri-grams:", tri_gram)
        print("\n")
        max_prints -= 1
        if max_prints == 0:
            break
