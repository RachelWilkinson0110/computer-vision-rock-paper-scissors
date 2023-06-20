"""
Importing needed modules to create the code for a game of rock paper scissors.

"""
import random
import time 
import cv2
import numpy as np
from keras.models import load_model
model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    
def get_computer_choice():
    """
    This function is used to randomly choose between the three options in this game - rock, paper or scissors
     """
    global computer_choice
    options=["Rock", "Paper", "Scissors"]
    computer_choice=random.choice(options)
    print(f"Computer choice: {computer_choice}")


def get_camera():

    """
    This function turns on the camera for the user input. This function will be called in the get_user_choice function.
    """
    end_time=time.time() +5
    while time.time()< end_time:
        ret, frame = cap.read()
        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'): 
            break
        

def countdown():

    """
    Normally, when you play rock, paper, scissors there is a 3 second countdown before each person reveals their hand gestures. 
    This function implements that 3 second countdown
    """
    countdown=3
    print("\nShow me your hand gesture in...")
    while countdown> 0:
        print(f'{countdown}')
        cv2.waitKey(1000)
        countdown -= 1 
    print("\nShow me your hand now!")     

def get_user_choice():
    """
    This function gets the users choice of hand gesture via the camera function.
    The model will predict which hand gesture the user is making by using probabilities. 
    We must select the getsure with the highest probability and assign it as the users choice - for this we have used the max function.
    """
    data[0]=get_camera()
    prediction=model.predict(data) 
    choice_probability = {'Rock': prediction[0,0], 'Paper': prediction[0,1], 'Scissors': prediction[0,2], "Nothing": prediction[0,3]}
    global user_choice
    user_choice=max(choice_probability, key=choice_probability.get)
    print(f"The model predicted that the user chose {user_choice}")
         

def get_winner():

    """
    This function is used to determine who won the round of rock, paper, scissors based on thier input- the computer or the user.
    This function also keeps track of the number of wins so we can determine which player reaches 3 wins first.
    """
    user_wins=0
    computer_wins=0
    while computer_wins<=2 and user_wins <=2:
        get_computer_choice()
        countdown()
        get_user_choice()
        if computer_choice==user_choice:
             print("It's a tie")
        elif computer_choice=="Rock":
            if user_choice=="Paper":
                user_wins+=1
                print(f"The computer choose {computer_choice}. Paper covers rock - You win!")
            else:
                computer_wins+=1
                print(f"The computer choose {computer_choice}. Rock beats scissors - You lose")
               
        elif computer_choice=="Scissors":
            if user_choice=="Rock":
                user_wins+=1
                print(f"The computer choose {computer_choice}. Rock beats scissors - You win!")      
            else:
                computer_wins+=1
                print(f"The computer choose {computer_choice}.  Scissors cuts paper - You lose")
                
        elif computer_choice=="Paper":
            if user_choice=="Scissors":
                user_wins+=1
                print(f"The computer choose {computer_choice}. Scissors cuts paper - You win!")
            else:
                computer_wins+=1
                print(f"The computer choose {computer_choice}. Paper covers rock - You lose")
        print (f"Score - Computer {computer_wins}: User {user_wins}")
        if computer_wins==3 or user_wins==3:
            print(f"First to 3 wins - Computer {computer_wins}: User {user_wins} - GAME OVER")
            break

def play():   
    get_winner()
        
    cap.release()
    cv2.destroyAllWindows()
        
play()
