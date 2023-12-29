import spacy
nlp = spacy.load("en_core_web_sm")
complete_text = (
     "Gus Proto is a Python developer currently"
     " working for a London-based Fintech company. He is"
     " interested in learning Natural Language Processing."
     " There is a developer conference happening on 21 July"
     ' 2019 in London. It is titled "Applications of Natural'
     ' Language Processing". There is a helpline number'
     " available at +44-1234567891. Gus is helping organize it."
     " He keeps organizing local Python meetups and several"
     " internal talks at his workplace. Gus is also presenting"
     ' a talk. The talk will introduce the reader about "Use'
     ' cases of Natural Language Processing in Fintech".'
     " Apart from his work, he is very passionate about music."
     " Gus is learning to play the Piano. He has enrolled"
     " himself in the weekend batch of Great Piano Academy."
     " Great Piano Academy is situated in Mayfair or the City"
     " of London and has world-class piano instructors."
 )

complete_doc = nlp(complete_text)
#A Doc object is a sequence of Token objects representing a lexical token.
#print([(token.text,token.idx) for token in complete_doc])

#Sentences detection
sentences = list(complete_doc.sents)
#print("There are",len(sentences),"sentences")
#for sentence in sentences:
#     print(f"{sentence[:5]}...")

#English stopwords
spacy_stopwords = spacy.lang.en.stop_words.STOP_WORDS
#print(len(spacy_stopwords))
#Print tokens that are not stopwords
#print([token for token in complete_doc if not token.is_stop])

