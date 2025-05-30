"""
   Author : Muhammed Adil
   Student number: 753209
   Course code: ICS3U
   Revison date : March 15, 2025
   Program : A number guessing game
   Description : a prgoram that will guess anumber between 1 & 100,
      and the user has to gues that number in the given 6 attempts. 
   VARIABLE DICTIONARY :
     num (int) = randomly generated number between 1 and 100  
     guess (int) = counter to track the number of guesses made by the user  
     guess_num (int) = user's guessed number inputted during the game  
"""

# Imports the random module to generate a random number.
import random  

# Prints a welcome message to the user.
print("Hello! Welcome to the number guessing game!")
# Tells the the user about the game and how it functions.
print("I am thinking of a number between 1 and 100. It is your turn to guess what it is.")
# Tells user how many tries they have to guess.
print("You have a maximum of six (6) tries.")

# Generates a random integer between 1 and 100 and assigns it to "num".
num = random.randint(1, 100) 
# Creates the variable "guess" (representing number of guesses) and assigns it to zero.
guess = 0

# Loops until the user has guessed 6 times.
while guess < 6:  
   # Increments the guess counter by one, each guess.
  guess += 1  
   # Asks the user for input, converts it to an integer, and stores it in guess_num (represents the number user guessed).
  guess_num = int(input("Guess #%d: " % guess))  

  # If the guessed number is equal to the randomly generated number, code below will run. 
  if guess_num == num:
    # Tells the user they guessed correctly.
    print("You guessed right!")  
    # Exits the loop since the correct number was guessed.
    guess = 7   
    # If the guess is too high:
  elif guess_num > num:  
      # Tells the user to guess a lower number.
      print("Lower!")  
    # If the guess is too low:
  else: 
      # Tells the user to guess a higher number.
      print("Higher!")

# If the loop was over and the user didn't correctly the code below will run.
if guess_num != num:
  # Tells the user they are out of guesses and tells them the correct number.
  print("Sorry: you are out of guesses! The answer was %d. Better luck next time!" % num)
