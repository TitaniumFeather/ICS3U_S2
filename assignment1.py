import math
change_original = int(input("Please enter the amount of change in cents: "))
change = change_original

amount_quarters = 0
amount_dimes = 0
amount_nickels = 0
amount_pennies = 0
amount_dollars = 0

if change >= 100:
  amount_dollars = math.trunc(change/100)
  change = change % 100

if change > 25:
  amount_quarters = math.trunc(change/25)
  change = change % 25
  
if 10 <= change < 25:
  amount_dimes = math.trunc(change/10)
  change = change % 10
  
if 5 <= change < 10:
  amount_nickels = math.trunc(change/5)
  change = change % 5

if 1<= change < 5:
  amount_pennies = math.trunc(change/1)
  change = change % 1

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
  
if amount_dollars == 1:
  dollar_text = "dollar"
elif amount_dollars > 1:
  dollar_text = "dollars"
else:
  dollar_text= ""
  amount_dollars = ""

if change == 0:
  print(f"{change_original} cents can be {amount_dollars} {dollar_text} {amount_quarters} {quarter_text} {amount_dimes} {dime_text} {amount_nickels} {nickel_text} {amount_pennies} {penny_text}.")
