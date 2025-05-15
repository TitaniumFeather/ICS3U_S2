#given code:
#import math
#x = input("Please input a whole number: ")
#x = int(x)
#y = input("Please input another nonzero whole number")
#y = int(y)
#print("Now deciding if", y, "is a factor of", x, "...")
#rem = x % y
#if rem == 0:
    #print("Yes!", y, "is a factor of", x)

#Predict:
#Code will ask user for whole number
#Code will then conver tthe string input to integer
#Code will ask for another non zero number and convert it to int
#Code will log the text "Now deciding if", y, "is a factor of", x, "..."
#If remainder between two numbers is 0, code will print "Yes!", y, "is a factor of", x

#Inspect:
#Yes it did match the output of my calculator when I tried dividing x by y

#Modify:
import math
x = int(input("Please input a whole number: "))
if 1 <= x <= 20:
    y = int(input("Please input another nonzero whole number"))
    if 1 <= y <= 20:
        if y != 0:
          print("Now deciding if", y, "is a factor of", x, "...")
          rem = x % y
          if rem == 0:
            print("Yes!", y, "is a factor of", x)
          else:
            print("No!", y, "is not a factor of", x)
    else:
        print("Enter number between 1 and 20")
else:
    print("Enter number between 1 and 20")



