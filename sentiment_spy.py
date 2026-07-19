from textblob import TextBlob
sentence=input("Enter how you are feeling: ")
blob=TextBlob(sentence)
sentiment=blob.sentiment.polarity
if sentiment>0:
    print("Positive sentiment")
elif sentiment==0:
    print("Neutral sentiment")
else:
    print("Negative Sentiment")