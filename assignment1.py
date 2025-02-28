############ PART 1: EVEN OR ODD ################
print("Welcome to the even and odd detector!")
print("This program determines if the product of two whole positive numbers will be even or odd!")

number_one = int(input("Please enter your 1st number: "))
number_two = int(input("Please enter your 2nd number: "))
product = number_one*number_two

if (number_one % 2 == 1 and number_two % 2 == 1):
    print(f"The product of {number_one} x {number_two} (which is {product}) will be odd.")
elif (number_one % 2 == 0 and number_two % 2 == 0):
    print(f"The product of {number_one} x {number_two} (which is {product}) will be even.")
elif (number_one % 2 == 1 and number_two % 2 == 0):
    print(f"The product {number_one} x {number_two} (which is {product}) will be even.")
else:
    print(f"The product {number_one} x {number_two} (which is {product}) will be even.")

############ PART 2: INNER DIAGONAL OF CUBE ################

import math
print("This program will find the cube's inner diagonal from any edge length!")

edge_length = int(input("Please enter the edge length of your cube: "))
diagonal = edge_length * math.sqrt(3)
diagonal = round(diagonal, 2)
print(f"The length of the inner diagonal of a cube with side length {edge_length} is: {diagonal}")

############ PART 3: CHANGE IN COINS ################

# Asks user to enter the amount of change in cents and store it as an integer in the "change_original variable".
change_original = int(input("Please enter the amount of change in cents: "))
# Creates a copy of change_original variable that can be changed and used in the code while change_original variable doesn't change and an be printed at the end of code for user (eg. number user intially put).
change = change_original

amount_quarters = 0 # amount of quarters that can be made form user change input
amount_dimes = 0 # amount of dimes that can be made form user change input
amount_nickels = 0 # amount of nickels that can be made from user change input
amount_pennies = 0 # amount of pennies that can be made from user change input
amount_dollars = 0 # amount of dollars that can be made from user change input

amount_dollars = int(change / 100)  # This line will calculate number of hundred cents in the change (dollars) 
change_original = change - (change - (change % 100))  # Updates the "change_original" variable value to be only the change (value below 100 cents) 
change = change - (change - (change % 100))  # Removes dollar value from change inputted by user

amount_quarters = int(change / 25)  # This line finds the number of quarters needed by dividing "change" by 25 (25 cents in a quarter) and uses "int" to make sure amount of quarters is an integer.
change = change % 25  # Updates the remaining change after quarter values taken away from change

amount_dimes = int(change / 10)  # Calculates number of dimes by dividing change by 10 and removing and decimals by using "int" so "amount_nickels" is a whole number
change = change % 10  # Updates the remaining change after dime values are remove for "change" variable

amount_nickels = int(change / 5)  # Calculates number of nickels by dividing change by 5 and removing and decimals by using "int" so "amount_nickels" is a whole number
change = change % 5  # Updates remaining change 

amount_pennies = change  # Amount of pennies should equal the remaining change as a penny is one cent so no division needed unlike the other coins.
change = change % 1  # Updates remaining change (should be 0)

print(change_original, "can be ", end="")
# This set of if and else statements adjusts the value of "quarter_text" to be plural (quarters) or singular (quarter) based on the amount_quarters used in change.
if amount_quarters == 1: # if amount of quarters is singular (only one quarter), execute indented code.
    print("%d quarter", % amount_quarters, end="")
elif amount_quarters > 1: # if amount of quarters is plural (more than one quarter), execute indented code.
    print("%d quarters", % amount_quarters, end="")
else: #this will run if there are zero quarters
    print("")  # if no quarters, leave empty

# This set of if and else statements adjusts the value of "dime_text" to be plural (dimes) or singular (dime) based on the "amount_dimes" used in change.
if amount_dimes == 1: # if amount of dimes is singular (only one dime), execute indented code.
    print("%d dime", % amount_dimes, end="") # this will change dime_text to be the number of dimes followed by the singular reference "dime".
elif amount_dimes > 1: # if amount of dimes is plural (more than one dime), execute indented code.
    print("%d dimes", % amount_dimes, end="") # this will change dime_text to be the number of dimes followed by the plural reference "dimes".
else: #this will run if there are zero dimes
    print("")  # If no dimes, leave empty

if amount_nickels == 1:
    print("%d nickel", % amount_nickels, end="")
elif amount_nickels > 1:
    print("%d nickels", % amount_nickels, end="")
else:
    print("")

if amount_pennies == 1:
    print("%d penny", % amount_pennies)
elif amount_pennies > 1:
    print("%d pennies", % amount_pennies)
else:
    penny_text = ""  # If no pennies, leave empty

# Construct the final result string with proper formatting
if change_original > 0:
    result = ""  # Initialize result string
    if quarter_text != "":  
        result += quarter_text + ", "  # Add quarters if they exist
    if dime_text != "":
        result += dime_text + ", "  # Add dimes to result if they exist (meaning they are not blank quotes "").
    if nickel_text != "":
        result += nickel_text + ", "  # Add nickels if they exist
    if penny_text != "":
        result += penny_text + ", "  # Add pennies if they exist

# Remove any trailing comma and space
result = result.strip(", ")

# Find the last comma in the result string
last_comma = result.rfind(", ")

# If a comma is found, replace the last comma with " and" to make the sentence grammatically correct
if last_comma != -1:
    result = result[:last_comma] + " and" + result[last_comma + 1:]

# Print the final result showing the change breakdown
print(f"{change_original} cents can be {result}.")
