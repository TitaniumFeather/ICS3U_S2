############# PART 1: EVEN OR ODD ################

# This line will print a welcome message to the user
print("Welcome to the even and odd detector!")
# This will tell the user that this program will determine if the product of two numbers will be even or odd
print("This program determines if the product of two whole positive numbers will be even or odd!")

number_one = int(input("Please enter your 1st number: ")) # creates int varaible "number_one" which is the user's chosen first number.
number_two = int(input("Please enter your 2nd number: ")) # creates int varaible "number_two" which is the user's chosen second number.
product = number_one * number_two # multiplies first number by second number and stores in the variable "product".

if (number_one % 2 == 1 and number_two % 2 == 1): # This will check if both numbers are odd (if that is true the statement below will run)
    print("The product of %d x %d (which is %d) will be odd." % (number_one, number_two, product))  # If both numbers are odd, it prints that the product (product value) will be odd
elif (number_one % 2 == 0 and number_two % 2 == 0): # This will check if both numbers are even (if that is true the statement below will run)
    print("The product of %d x %d (which is %d) will be even." % (number_one, number_two, product)) # If both numbers are even, it prints that the product will be even to the console
elif (number_one % 2 == 1 and number_two % 2 == 0): # This will check if "number_one" is odd and "number_two" is even (if that is true the statement below will run)
    print("The product %d x %d (which is %d) will be even." % (number_one, number_two, product)) # If first is odd and second is even, it prints that the product will be even
else: # If the first number is even and the second is odd
    print("The product %d x %d (which is %d) will be even." % (number_one, number_two, product)) # If first is even and second is odd, it prints that the product will be even


############ PART 2: INNER DIAGONAL OF CUBE ################

# Imports the math module to use the math function such as square root which will be used later on in code
import math
# Tells user that my program will find the inner diagonal of a cube based of their given side length
print("I will find the cube's inner diagonal for any edge length!")
# Asks the user to enter their chosen edge length of the cube and stores it as an integer in "edge_length" variable
edge_length = int(input("Please enter the edge length of your cube: "))
# Calculates the diagonal using the formula for the diagonal of a cube which is just edge * sqrt(3)
diagonal = edge_length * math.sqrt(3)
# This line rounds the diagonal to 2 decimal places by using "round" method
diagonal = round(diagonal, 2)
# This prints the diagonal in a sentence format that tells the user the two numbers they multiplied, its product and whether it's even or odd
print("The length of the inner diagonal of a cube with side length %d is: %.2f" % (edge_length, diagonal))

############ PART 3: CHANGE IN COINS ################

# Asks the user to input the amount of change in cents and stores it as an integer in change_original
change_original = int(input("Please enter the amount of change in cents: "))
# Creates a copy of change_original so that the original value can be printed later without modification
change = change_original

amount_quarters = 0 # amount of quarters
amount_dimes = 0 # amount of dimes
amount_nickels = 0 # amount of nickels
amount_pennies = 0 # amount of pennies
amount_dollars = 0 # amount of dollars

# Calculates how many whole dollars (100 cents) can be made from the change
amount_dollars = int(change / 100)
# Updates change_original to hold only the cents less than 100 (the remainder)
change_original = change - (change - (change % 100))
# Removes the dollar value from the change
change = change - (change - (change % 100))

# Finds value of "amount_quarters" (how many quarters) in integer form by dividing change by 25 "cents"
amount_quarters = int(change / 25)
# Updates the remaining change after removing the quarters
change = change % 25

# Finds value of "amount_dimes" (how many dimes) in integer form by dividing change by 10 "cents"
amount_dimes = int(change / 10)
# Updates the remaining change after removing the dimes
change = change % 10

# Finds value of "amount_nickels" (how many nickels) in integer form by dividing change by 5 "cents"
amount_nickels = int(change / 5)
# This will update "change" to be the remaining change after removing the nickels
change = change % 5

# The remaining change is all in pennies (1 cent each), so amount_pennies equals the remaining change
amount_pennies = change
# Updates the remaining change (should now be 0) as one penny is a cent
change = change % 1

# Creates sentence starter for ouput by telling user the amount of change the user oroginally entered
print("%d cents can be" % change_original, end="")

# If there is exactly 1 quarter, it prints "1 quarter"
if amount_quarters == 1:
    print(" %d quarter" % amount_quarters, end="")
# If there are more than 1 quarter, it prints the number of quarters with the plural form
elif amount_quarters > 1:
    print(" %d quarters" % amount_quarters, end="")

# If there is exactly 1 dime, it handles the singular form "dime"
if amount_dimes == 1:
    # Checks if there are no other coins as and adds "and" before the word "dime"
    if amount_nickels == 0 and amount_pennies == 0 and amount_quarters > 0:
        print(" and %d dime" % amount_dimes, end="")
    else:
        print(", %d dime" % amount_dimes, end="")
# If there is more than 1 dime, it handles the plural form "dimes"
elif amount_dimes > 1:
    # Checks if there are no other coins and adds "and" before the word "dimes"
    if amount_nickels == 0 and amount_pennies == 0 and amount_quarters > 0:
        print(" and %d dimes" % amount_dimes, end="")
    else:
        print(", %d dimes" % amount_dimes, end="")

# If there is exactly 1 nickel, it handles the singular form "nickel"
if amount_nickels == 1:
    # Checks if there are no pennies, and adds "and" before the word "nickel"
    if amount_pennies == 0 and (amount_quarters > 0 or amount_dimes > 0):
        print(" and %d nickel" % amount_nickels, end="")
    else:
        print(", %d nickel" % amount_nickels, end="")
# If there are more than 1 nickel, it handles the plural form "nickels"
elif amount_nickels > 1:
    # Checks if there are no pennies, and adds "and" before the word "nickels"
    if amount_pennies == 0 and (amount_quarters > 0 or amount_dimes > 0):
        print(" and %d nickels" % amount_nickels, end="")
    else:
        print(", %d nickels" % amount_nickels, end="")

# If there is exactly 1 penny, it handles the singular form "penny"
if amount_pennies == 1:
    # Checks if there are other coins and adds "and" before the word "penny"
    if amount_quarters > 0 and amount_nickels > 0 and amount_dimes > 0:
        print(" and %d penny" % amount_pennies, end="")
    else:
        print(", %d penny" % amount_pennies, end="")
# If there are more than 1 penny, it handles the plural form "pennies"
elif amount_pennies > 1:
    # Checks if there are other coins and adds "and" before the word "pennies"
    if amount_quarters > 0 or amount_nickels > 0 or amount_dimes > 0:
        print(" and %d pennies" % amount_pennies, end="")
    else:
        print(", %d pennies" % amount_pennies, end="")

# Adds a final period after the output
print(".")
