# Task A:
# given code:
print("Welcome to Sanjay's Koala Party!")
print("It's possible Sanjay can distribute ", 12)
print(" cookies for each bowl.")
# Reflection:
# I think that it will output the following in different lines:
  # "Welcome to Sanjay's Koala Party!"
  # It's possible Sanjay can distribute  12
  #  cookies for each bowl.
# When I ran the program, my prediction was correct
# Fix the program so that there is only one space before and after the "12":
print("Welcome to Sanjay's Koala Party!")
print("It's possible Sanjay can distribute", 12)
print("cookies for each bowl.")


# Task B:
# Sanjay has 6 bowls for 144 cookies.
print("Sanjay has", 6, "bowls for", 144, "cookies.")
# We can do it using another methood with placeholders like. In our case we use %d (integers):
print("Sanjay has %d bowls for %d cookies." % (6, 144))


# Task C:
print("The number of cookies per bowl is:", 144/6)
# There is one text value and one number value (two numbers being divided with the / operator)
