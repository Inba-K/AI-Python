from textblob import TextBlob
c="yes"
positive=0
neutral=0
negative=0
summary=0
help=0
a=input("What do you need help with? ")
while c=="yes":
    if a=='sentiment':
        sentence=input("How are you feeling? ")
        blob=TextBlob(sentence)
        sentiment=blob.sentiment.polarity
        if sentiment<0:
            print("Negative sentiment")
            print("-------------------------")
            negative+=1
        elif sentiment==0:
            print("Neutral sentiment")
            print("-------------------------")
            neutral+=1
        else:
            print("Positive sentiment")
            print("-------------------------")
            positive+=1
    elif a=='help':
        print("Command 1: help (displays function of this bot)")
        print("Command 2: sentiment (emotion detection)")
        print("Command 3: summary (of what you did)")
        print("-------------------------")
        help+=1
    elif a=='summary':
        summary+=1
        print("SUMMARY:")
        print(positive,"positive sentiment(s)")
        print(neutral,"neutral sentiment(s)")
        print(negative,"negative sentiment(s)")
        print(summary,"summary or summaries")
        print(help,"time(s) asked for help")
        print("-------------------------")
    else:
        print("I didn't understand... You can use the 'help' function of you want to see the functions...")
        print("-------------------------")
    c=input("Would you like to continue? ")
    if c!="yes" and c!="Yes":
        print("Nice chatting!")
        break
    a=input("What else can I help with? ")
