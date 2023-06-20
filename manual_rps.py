import random

def get_computer_choice():
    options=["rock", "paper", "scissors"]
    global computer_choice
    computer_choice=random.choice(options)
    print(computer_choice)
    


def get_user_choice():
    global user_choice
    user_choice=input("Please choose rock, paper or scissors?")
    
    

def get_winner(computer_choice, user_choice):

    if computer_choice==user_choice:
        print("It's a tie")
    elif computer_choice=="rock":
        if user_choice=="paper":
            print("You win!")
        else:
            print("You lose")
    elif computer_choice=="scissors":
        if user_choice=="rock":
            print("You win!")
        else:
            print("You lose")
    elif computer_choice=="paper":
        if user_choice=="scissors":
            print("You win!")
        else:
            print("You lose")



def play():
    get_computer_choice()
    
    get_user_choice()
    get_winner(computer_choice, user_choice)

play()
