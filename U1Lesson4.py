#given code:
    #num = input("Please input a whole number: ") 
    #num = int(num) 
    #num2 = num / 6
    #print("When", num, " is divided by 6", "the result is:", num2)
# Predict:
# I predict that the code will print Please input a whole number: and wait for the user to input something into the console
# It will then print When (the number entered by the user)  is divided by 6 the result is: (result of the number divided by 6)
# For example if I input the number 18, it will output:
# Please input a whole number:  18
# When 18  is divided by 6 the result is: 3.0

# Run
# When I ran the code my prediction was correct

# Inspect
# When it stopped execution, it stopped because of the use of input() in the code and the code is waiting for the user to input something into the console

# Modify
num = input("Please input a whole number: ")
num2 = input("Use any whole number except zero: ")
num = int(num)
num2 = int(num2)
num3 = num / num2
print("When", num, "is divided by", num2, "the result is:", num3)
# The exception "Use any whole number except zero" is needed because you can not divide by 0 and python will crash
