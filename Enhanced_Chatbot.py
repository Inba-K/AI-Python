import datetime
a=input("What is your name? ")
print("Hello",a,"! What can I help you with?")
b=input()
c="yes"
while c=="yes":
    if "time" in b:
        print("No problem! The time is",datetime.datetime.now().time())
    elif "date" in b:
        print("Got it! The date is",datetime.datetime.now().date())
    elif "weather" in b:
        print("The weather is looking very hot today, as expected in July!")
    elif "joke" in b:
        print("Here's a joke! What do you call a bird without a beak?")
        d=input()
        if "ird" in d:
            print("That's right!")
        else:
            print("An ird!")
    print("What else can I help you with,",a,"?")
    b=input()
    if "nothing" in b:
        print("Nice chatting,",a,"!")
        break