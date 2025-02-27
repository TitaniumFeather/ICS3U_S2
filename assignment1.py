change_original = int(input("Please enter the amount of change in cents: "))
change = change_original

amount_quarters = 0
amount_dimes = 0
amount_nickels = 0
amount_pennies = 0
amount_dollars = 0
list = []

if change >= 100:
  amount_dollars = math.trunc(change/100)
  change_original = change - (change - (change % 100))
  change = change - (change - (change % 100))

if change >= 25:
  amount_quarters = int(change/25)
  change = change % 25
  
if 10 <= change < 25:
  amount_dimes = int(change/10)
  change = change % 10
  
if 5 <= change < 10:
  amount_nickels = int(change/5)
  change = change % 5

if 1<= change < 5:
  amount_pennies = int(change/1)
  change = change % 1

if amount_quarters == 1:
  quarter_text = str(amount_quarters) + " quarter,"
elif amount_quarters > 1:
  quarter_text = str(amount_quarters) + " quarters,"
else:
  quarter_text= ""
  amount_quarters =""

if amount_dimes == 1:
  dime_text = str(amount_dimes) + " dime,"
elif amount_dimes > 1:
  dime_text = str(amount_dimes) + " dimes,"
else:
  dime_text= ""
  amount_dimes = ""

if amount_pennies == 1:
  penny_text = str(amount_pennies) + " penny,"
elif amount_pennies > 1:
  penny_text = str(amount_pennies) + " pennies,"
else:
  penny_text= ""
  amount_pennies = ""

if amount_nickels == 1:
  nickel_text = str(amount_nickels) + " nickel,"
elif amount_nickels > 1:
  nickel_text = str(amount_nickels) + " nickels,"
else:
  nickel_text= ""
  amount_nickels = ""
  

if change == 0:
  print(f"{change_original} cents can be {quarter_text} {dime_text} {nickel_text} {penny_text}.")
