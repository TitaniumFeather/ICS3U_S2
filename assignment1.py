import math
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
  quarter_text = str(amount_quarters) + " quarter,"
  list.append(quarter_text)
elif amount_quarters > 1:
  quarter_text = str(amount_quarters) + " quarters,"
  list.append(quarter_text)
else:
  quarter_text= ""
  amount_quarters =""

if amount_dimes == 1:
  dime_text = str(amount_dimes) + " dime,"
  list.append(dime_text)
elif amount_dimes > 1:
  dime_text = str(amount_dimes) + " dimes,"
  list.append(dime_text)
else:
  dime_text= ""
  amount_dimes = ""

if amount_pennies == 1:
  penny_text = str(amount_pennies) + " penny"
  list.append(penny_text)
elif amount_pennies > 1:
  penny_text = str(amount_pennies) + " pennies"
  list.append(penny_text)
else:
  penny_text= ""
  amount_pennies = ""

if amount_nickels == 1:
  nickel_text = str(amount_nickels) + " nickel,"
  list.append(nickel_text)
elif amount_nickels > 1:
  nickel_text = str(amount_nickels) + " nickels,"
  list.append(nickel_text)
else:
  nickel_text= ""
  amount_nickels = ""

list.insert(-1, "and")
list[-1] = list[-1].replace(',', '')
joinedList = ' '.join(list)

if change == 0:
  print(f"{change_original} cents can be {joinedList}.")
