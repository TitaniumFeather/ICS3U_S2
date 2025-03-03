# Predict: The code will output "I prefer cherries".

# Reflection: My prediction was correct as the code outputted the above. When we enter a letter asides from A, B and C the code outputs "I prefer cherries" for all other letters/symbols. This is a problem because "C" is the only letter/symbol that should represnt cherries, but in thhis case any letter/symbol aside from A & B can represent.

# Modify 1:
print("Make a choice from the following menu: ")
print("A: apples")
print("B: bananas")
print("C: cherries")

ch = input("Your choice: ")

if (ch == "A"):
    print("I prefer apples")
elif (ch == "B"):
    print("I prefer bananas")
elif (ch == "C"):
    print("I prefer cherries")
else:
    print("Please enter either A, B or C")

#Mdoify 2:
if (x >= 80) and (x <= 100)
