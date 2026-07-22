import random
print("Welcome to the rock paper scissors game")
options=['rock','paper','scissors']
play='yes'
while play=='yes' or play=='Yes':
    player_decision=input("Choose between rock, paper, and scissors: ")
    computer_decision=random.choice(options)
    if player_decision==computer_decision:
        print("It's a draw")
        print(player_decision,computer_decision)
    elif player_decision=='rock' and computer_decision=='scissors':
        print(player_decision,computer_decision)
        print("You win!")
    elif player_decision=='scissors' and computer_decision=='paper':
        print(player_decision,computer_decision)
        print("You win!")
    elif player_decision=='paper' and computer_decision=='rock':
        print(player_decision,computer_decision)
        print("You win!")
    elif player_decision!='rock' and player_decision!='paper' and player_decision!='scissors':
        print("You must choose between rock, paper, and scissors.")
    else:
        print(player_decision,computer_decision)
        print("You lose...")
    play=input("Would you like to keep playing? ")
    if play!='yes' and play!='Yes':
        print("Thanks for playing!")
        break