word = input("Enter a word: ")

arr = list(word)
counter = 0

for i in range(len(arr)):
  if arr[i] == arr[-1 - i]:
   counter +=1
  else:
    print(word, "is not a palindrome!")
    break
  if counter == len(arr):
    print(word, "is a palindrome!")
     
  
