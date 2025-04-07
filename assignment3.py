print("Palindrome program!")
palindromeArray = ["civic", "basketball", "radar", "goal", "kayak", "soccer", "racecar", "hotel", "refer", "loop"]

for word in palindromeArray:
  letterMatches = 0
  letterPosition = 0
  halfway = len(word) // 2
  while letterPosition < halfway:
    if word[letterPosition] == word[len(word) - 1 - letterPosition]:
      letterMatches += 1
    else:
      print(word, "is not a palindrome!" )
      letterPosition = halfway
    if letterMatches == halfway:
      print(word, "is a palindrome!" )
    letterPosition += 1
    
print("Goodbye!")
     
  

