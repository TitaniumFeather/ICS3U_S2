lengthList = int(input("How many items are you entering? "))
fruits = []
inputs = 0
print("Enter your items now:")
while inputs < lengthList:
  item = input("Next item:")
  fruits.append(item)
  inputs += 1

length = len(fruits)
print("You have %d items." % length)
for m in range(length):
  print(fruits[m])
