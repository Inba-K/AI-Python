import datetime
a=input("What is your name? ")
b=int(input("What is your age? "))
print("Hello",a,", how can I help you?")
c=input()
if "date" in c:
    print("Today's date is",datetime.datetime.now().date())
elif "time" in c:
    print("The time is",datetime.datetime.now().time())