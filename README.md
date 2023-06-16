# Computer Vision RPS

I created a separate environemnt named CV and specified that this environment should use version 3.8 of python. I did this using conda create -n "CV" python =3.8.

I then created 3 separate functions - get_computer_choice, get_user_choice and get_winner.
get_computer_choice uses the random module (random.choice()) to choose a random option from the list rock, paper, scissors.

get_user_choice takes user input for either rock, paper or scissors.

get_winner uses both the computer_choice and user_choic to determine who wins the game. The relevant output is then printed - 'It's a tie', 'You win' or 'You lose'.

I then called this 3 functions within one final function - play().

