#Instructions:
#The user is asked for their year of birth and their age.
#Double the birth year, then add 5.
#Multiply the resyult of the last step by 50, then add their age.
#Subtract 250 from the result of the last calculation, then divide by 100.
#Print the result and interpret it for the user.

age = int(input("Enter your age: "))
birth = int(input("Enter your birth year: "))
x = ((((birth+birth) + 5)*50 + age) - 250)/100
print("Your birth year followed by decimal (age) is: ",x)

