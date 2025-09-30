import nltk

nltk.download("punkt_tab") #or punkt lang is english

sentence = "ang baliw ng mundo"

token = nltk.word_tokenize(sentence)
sentence_token = nltk.sent_tokenize(sentence)

print("Word Token:", token)
print("Sentence Token:", sentence_token)