print("Palindrom program!")
palindromeArray = ["civic", "basketball", "radar", "level", "kayak", "soccer", "racecar", "madam", "refer", "lool"]

counter = 0

for word in palindromeArray:
  maxNum = len(word)//2
  for j in range(maxNum):
    if word[j] == word[len(word)-1-j]:
      counter +=1
    else:
      print(word, "is not a palindrome!" )
      break
    if counter == maxNum:
      print(word, "is a palindrome!" )
     
  

