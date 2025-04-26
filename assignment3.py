"""
   Author : Muhammed Adil
   Student number: 753209
   Course code: ICS3U
   Revison date : April 25, 2025
   Program : Palindrome checker
   Description : A porgram that identifies whther the words in a given list are 
       palindromes or not.
   VARIABLE DICTIONARY :
     palindromeArray (list) = array of words with palindromes and non-palindromes 
     letterMatches (int) = amount of matches in the word between a letter and a letter
       from the mirroring side.
     letterPosition (int) = index indicating the letter in a word
     halfway (int) = half the length of a word
"""
# Informs user about the program details
print("Palindrome program!")
# Creates an array with words either palindrome 
palindromeArray = ["civic", "basketball", "radar", "goal", "kayak", "soccer", "racecar", "hotel", "refer", "loop"]

# Creates for loop that cycles through each word in the palindromeArray
for word in palindromeArray:
  # Creates variable which tracks the amount of matches between a letter and it's mirroring letter (set to 0)
  letterMatches = 0
  # Create variable which tracks the index of a letter in chsoen word (set to 0)
  letterPosition = 0
  # Creates variable which represents halway of chosen word
  halfway = len(word) // 2
  
  # Loops through the first half of the word
  while letterPosition < halfway:
     
    # Compares the letter at the current position with its mirrored letter from the end
    if word[letterPosition] == word[len(word) - 1 - letterPosition]:
      # If letters match, increment the match count
      letterMatches += 1
      # Move to the next letter position
      letterPosition += 1
    # If letters don't match:
    else:
      # print word is not palindrome
      print(word, "is not a palindrome")
      # Exits the loop
      letterPosition = halfway
      
    # If all mirrored letter pairs matched:
    if letterMatches == halfway:
      # print the word is a palindrome
      print(word, "is a palindrome")

# Informs user that the program has ended
print("Goodbye!")
