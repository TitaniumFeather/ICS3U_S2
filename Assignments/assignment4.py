# Open file and assigns it to "fh"


# Creates an array that stores each line as a value
arr = []
# Creates array for all dates in number format
date_arr = []
# Creates array with all words in "wordle.dat"
word_arr = []
# Array with mopnths
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", 
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

try:
  fh = open("wordle.dat", "r")
  eof = False
  while not eof:
    line = fh.readline().strip()
    eof = (line == "")
  if not eof:
      arr.append(line.split(" "))
fh.close()

def merge(month, day, year):
  year = int(year) * 10000
  month = (months.index(month) + 1) * 100
  day = int(day)
  return year + month + day

for x in range(len(arr)):
  date_arr.append(merge(arr[x][0], arr[x][1], arr[x][2]))
  word_arr.append(arr[x][3])

def isWordMatch(user_word):
  counter = 0
  for word in word_arr:
    if word == user_word.upper():
      counter += 1
  if counter == 1:
    return date_arr[word_arr.index(user_word.upper())]
  else:
    return 0

def isDateMatch(month, day, year):
  counter = 0
  date = merge(month, day, year)
  for number in date_arr:
    if number == date:
      counter += 1
  if counter == 1:
    return word_arr[date_arr.index(date)]

print("Welcome to the Wordle Database!")
choice = input("Enter w if you are looking for a word, or d for a word on a certain date:")

if choice == "w":
  w = input("What word are you looking for? ")
  if isWordMatch(w) > 0:
    print("The word", w.upper(), "was the solution to the puzzle on", isWordMatch(w))
  else:
    print(w.upper(), "was not found in the database.")

elif choice == "d":
  user_year = input("Enter the year: ")
  user_month = input("Enter the month (3-letter abbreviation, as in 'Jan' for 'January'): ").capitalize()
  user_day = input("Enter the day: ")
  if 20210619 <= merge(user_month, user_day, user_year) <= 20240421:
    print("The word entered on", merge(user_month, user_day, user_year), "was", isDateMatch(user_month, user_day, user_year))
  elif 20210619 > merge(user_month, user_day, user_year):
    print(merge(user_month, user_day, user_year), "is too early. No wordles occurred before 20210619. Enter a later date.")
  else:
    print(merge(user_month, user_day, user_year), "is too recent. Our records only go as late as 20240421. Please enter an earlier date.")

else:
  print("Unrecognized option. Enter either 'w' or 'd'.")
