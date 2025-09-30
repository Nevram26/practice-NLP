from textblob import TextBlob

text = "Java programming language is ugly and bad"
blob = TextBlob(text)

print("polarity score: ", blob.sentiment.polarity)
print("Sub score: ", blob.sentiment.subjectivity)

print("Tokens:",blob.tokens)
print("POS tags: ", blob.tags)