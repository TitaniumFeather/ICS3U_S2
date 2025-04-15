# Informs user about the program details
print("Palindrome program!")
# Creates an array with words either palindrome 
palindromeArray = ["civic", "basketball", "radar", "goal", "kayak", "soccer", "racecar", "hotel", "refer", "loop"]

# Creates for loop that cycles through each word in the palindromeArray
for word in palindromeArray:
  # C
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
     
  

