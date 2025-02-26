change_original = int(input("Please enter the amount of change in cents: "))
change = change_original

amount_quarters = 0
amount_dimes = 0
amount_nickels = 0
amount_pennies = 0

if change >= 100:
  change -= 100

if change >= 200:
  change -= 200

if change >= 300:
  change -= 300
  
if change >= 400:
  change -= 400

if change >= 75:
  change -= 75
  amount_quarters += 3
  
if 50 <= change < 75:
  change -= 50
  amount_quarters += 2

if 25 <= change < 50:
  change -= 25
  amount_quarters += 1

if 15 <= change < 25:
  change -= 10
  amount_dimes += 1

if 10 <= change < 15:
  change -= 10
  amount_dimes += 1

if 5 <= change < 10:
  change -= 5
  amount_nickels +=1

if change == 4:
  change -= 4
  amount_pennies += 4

if change == 3:
  change -= 3
  amount_pennies += 3

if change == 2:
  change -= 2
  amount_pennies += 2

if change == 1:
  change -= 1
  amount_pennies += 1

if amount_quarters == 1:
  quarter_text = "quarter"
elif amount_quarters > 1:
  quarter_text = "quarters"
else:
  quarter_text= ""
  amount_quarters =""

if amount_dimes == 1:
  dime_text = "dime,"
elif amount_dimes > 1:
  dime_text = "dimes"
else:
  dime_text= ""
  amount_dimes = ""

if amount_pennies == 1:
  penny_text = "penny"
elif amount_pennies > 1:
  penny_text = "pennies"
else:
  penny_text= ""
  amount_pennies = ""

if amount_nickels == 1:
  nickel_text = "nickel"
elif amount_nickels > 1:
  nickel_text = "nickels"
else:
  nickel_text= ""
  amount_nickels = ""

if change == 0:
  print(f"{change_original} cents can be {amount_quarters} {quarter_text} {amount_dimes} {dime_text} {amount_nickels} {nickel_text} {amount_pennies} {penny_text}.")
