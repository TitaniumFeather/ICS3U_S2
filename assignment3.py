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
  # Creates variable which tracks the amount of matches between letters
  letterMatches = 0
  letterPosition = 0
  halfway = len(word) // 2
  
  while letterPosition < halfway:
    
    if word[letterPosition] == word[len(word) - 1 - letterPosition]:
      letterMatches += 1
      letterPosition += 1
    else:
      print(word, "is not a palindrome")
      letterPosition = halfway
      
    if letterMatches == halfway:
      print(word, "is a palindrome")

# 
print("Goodbye!")
     
  

