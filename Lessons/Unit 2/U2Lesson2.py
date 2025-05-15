# Part A
# Predict: I think the code will print number 9 all the way to number 1 in descending order.
# Refection: Prediction was correct.

#Modify 1:
count = 9
while (count != 0):
    count -= 1
    print(count)
# Predict: I think the code will print number 8 all the way to number 0 in descending order.

#Part B
adder = 0
number = 0
position = "1st"

while number <= 15:
  adder += 1
  number += adder
  if adder == 1:
    position = "st"
  elif adder == 2:
    position = "nd"
  elif adder == 3:
    position = "rd"
  else: 
    position = "th"
  print("Your %d%s triangular number is %d" % (adder, position, number))
  

