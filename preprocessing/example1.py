import spacy
nlp = spacy.load("en_core_web_sm")
doc=nlp("this is me in 1998 !")
print(doc)
# Iterate over the tokens
for token in doc:
    # Print the token and its part-of-speech tag
    print(token.text, "-->", token.pos_)
    # Print the token and its lemma
    print(token.text, "-->", token.lemma_)