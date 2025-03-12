"""
  A number guessing game where the program selects a random number between 1 and 20, 
  and the user must guess it. 
  Provide hints like "Too high" or "Too low".
  Make sure that the user is only entering values between 1 and 20 and the user has 
  maximum of 5 guesses. 
  If the user exceeds the max number of gusses then program
  should print "Game over!".

  Algorithm
  -----------------------
  Start
  Generate a random number between 1 and 20
  Set guess count to 1
  Repeat till User makes the correct guess or guess count reaches 5
  Accept the user input
  Verify the user input is between 1 and 20 and if not ask the user to input again
  If user input is less than random number print "Too Low"
  If user input is greater than random number print "Too High"
  If user input is same as random number print "Correct"
  End

"""
import random   # Python module named random

random_number = random.randint(1,20) # Generate a random number between 1 and 20

---------------------------------------------------------------------------------------------------------------------------------------------------------------------
Implementation in Python

import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    
    secret_number = random.randint(1, 20)
    
    max_attempts = 5
    attempts = 0
    
    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts + 1}/{max_attempts} - Enter a number (1-20): "))
            
            if guess < 1 or guess > 20:
                print("Invalid input! Please enter a number between 1 and 20.")
                continue  
            
            attempts += 1

            if guess < secret_number:
                print("Too Low!")
            elif guess > secret_number:
                print("Too High!")
            else:
                print(f" Correct! You guessed the number in {attempts} attempts!")
                return  

        except ValueError:
            print("Invalid input! Please enter a valid number.")
    
    print("Game Over! The correct number was:", secret_number)

number_guessing_game()


Output-
Welcome to the Number Guessing Game!
Attempt 1/5 - Enter a number (1-20): 12
Too High!
Attempt 2/5 - Enter a number (1-20): 10
Too Low!
Attempt 3/5 - Enter a number (1-20): 11
Correct! You guessed the number in 3 attempts!
