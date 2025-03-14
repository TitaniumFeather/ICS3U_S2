import random

print("Hello! Welcome to the number guessing game!")
print("I am thinking of a number between 1 and 100. It is your turn to guess what it is. You have a maximum of six (6) tries.")

num = random.randrange(1, 100, 1) 
guess = 0

while guess < 6: 
  guess += 1
  guess_num = int(input("Guess #%d: " % guess))

  if guess_num == num:
    print("You guessed right!")
    break
  elif guess < 6: 
    if guess_num > num:
      print("Lower!")
    else:
      print("Higher!")

if guess_num != num:
  print("Sorry: you are out of guesses! The answer was %d. Better luck next time!" % num)
