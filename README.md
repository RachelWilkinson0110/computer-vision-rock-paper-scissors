# Computer Vision RPS

Task: Create a game of Rock Paper Scissors using computer vision system.

**Rules of the Game**
Each player will have 3 choices - rock, paper or scissors.
There will be 2 players - the computer and the user.
The computer will randomly choose a gesture from the 3 options.
The user will be asked to choose a gesture and _show_ this gesture to the webcam.

There are three possible outcomes - win, lose, tie. 
The winner is determined based on the following:
* Rock beats Scissors
* Paper covers Rock
* Scissors cuts Paper

The game will end when the first player accumulates 3 wins.

**Steps to create the game**

## Numbered lists

Steps:

1. Create and Train a model 
This was done using Teachable Models. For each gesture between 500-700 images were used to train the model.
This model was then downloaded and implemented into the code to interpret the users chosen hand gesture.

2. Writing the code
I created a separate environemnt named CV and specified that this environment should use version 3.8 of python. I did this using conda create -n "CV" python =3.8.
I then created 3 separate functions - get_computer_choice, get_user_choice and get_winner.
_get_computer_choice_ uses the random module (random.choice()) to choose a random option from the list rock, paper, scissors.
_get_user_choice_ takes user input for either rock, paper or scissors using the webcam.
_get_winner_ uses both the computer_choice and user_choic to determine who wins the game. This fucntion records the number of wins for each player. A while loop is used to repeat the game until a player accumulates 3 wins.



