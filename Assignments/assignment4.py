"""
Author : Muhammed Adil
Student number: 753209
Course code: ICS3U
Revision date : May 17, 2025
Program : Wordle Database Search
Description : A program that reads from a Wordle solution file and allows the user to 
    search for a Wordle solution by date or find the date on which a specific word appeared.

VARIABLE DICTIONARY :
  arr (list) = stores each line of the file as a list: [Month, Day, Year, Word]
  date_arr (list) = stores all dates in integer YYYYMMDD format
  word_arr (list) = stores all the words from the file
  months (list) = contains month abbreviations used to convert month names to numbers
  fh (file object) = used to open and read the wordle.dat file
  line (str) = temporarily stores a line read from the file before processing
  month (str) = stores the 3-letter abbreviation of the month
  day (str) = stores the day portion of a date
  year (str) = stores the year portion of a date
  date (int) = temporary variable wehn looping through date_arr
  input_date (int) = result of merging user-entered month, day, and year
  word (str) = temporary variable used when looping through word_arr
  user_word (str) = stores the word input by the user when searching for a date
  choice (str) = stores user input for selecting either word or date search
  w (str) = stores the word input by the user if searching by word
  user_year (str) = stores the year input by the user when searching by date
  user_month (str) = stores the month input by the user when searching by date
  user_day (str) = stores the day input by the user when searching by date
"""

# Creates an array that stores each line as a value
arr = []
# Creates array for all dates in number format
date_arr = []
# Creates array with all words in "wordle.dat"
word_arr = []
# Array with months for converting 3-letter month to number
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", 
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

# Tries to open and read the "wordle.dat" file
try:
  # Opens the file in read mode
  fh = open("wordle.dat", "r")
  # Reads the first line and strips whitespace
  line = fh.readline().strip()
  # Continues until an empty line is checked (EOF)
  while line != "":
    # Splits line into parts and appends to arr (2d array)
    arr.append(line.split(" ")) 
    # Reads the next line
    line = fh.readline().strip()  
  # Closes the file after reading
  fh.close()  
except OSError as err:
  # Handles file not found error and prints message
  print("OSError: ", err)  

# Defines a function to convert date to an integer in YYYYMMDD format
def merge(month, day, year):
  # Turns year into YYYY0000
  year = int(year) * 10000
  # Turns month name to MM00
  month = (months.index(month) + 1) * 100  
  day = int(day)
  # Combines all into one integer an returns
  return year + month + day  

# Loops through each row in arr to fill date_arr and word_arr
for x in range(len(arr)):
  # Converts the date to int and appends to date_arr
  date_arr.append(merge(arr[x][0], arr[x][1], arr[x][2]))
  # Appends the word (third item in the row)
  word_arr.append(arr[x][3])  

# Creates function to search for a word and returns the date if found
def isWordMatch(user_word):
  # Cycles through every word in word_arr
  for word in word_arr:
    # Checks if equal to uppercase version of input
    if word == user_word.upper():
      # Returns the date at the same index of user_word in word_arr, and exits 
      return date_arr[word_arr.index(user_word.upper())]
  # Returns 0 if word not found in word_arr
  return 0  

# Defines function to search for a date and return the corresponding word
def isDateMatch(month, day, year):
  input_date = merge(month, day, year)  # Converts input date to integer
  # Cycles through every date in date_arr
  for date in date_arr:
    # if date is equal to input_date:
    if date == input_date:
      # Return the word at the same index of input_date, and exit
      return word_arr[date_arr.index(input_date)]  

print("Welcome to the Wordle Database!")  # Greeting message
# User choice
choice = input("Enter w if you are looking for a word, "
               "or d for a word on a certain date: ")  

# If user wants to search by word
if choice == "w":
  w = input("What word are you looking for? ")  # Gets word input
  # If the word has a matching date:
  if isWordMatch(w) > 0:
    # Displays date
    print("The word", w.upper(), "was the solution to the puzzle on", isWordMatch(w))  
  else:
    # Word not found
    print(w.upper(), "was not found in the database.")

# If user wants to search by date
elif choice == "d":
  user_year = input("Enter the year: ")  # User year
  # Gets user month and capitalizes first letter
  user_month = input("Enter the month (3-letter abbreviation, as in 'Jan' for 'January'): ").capitalize()  
  user_day = input("Enter the day: ")  # Gets day
  # Checks if date is within range
  if 20210619 <= merge(user_month, user_day, user_year) <= 20240421:  
    # Displays date and the corresponding word  
    print("The word entered on", merge(user_month, user_day, user_year), "was", isDateMatch(user_month, user_day, user_year))  
  # If date too early
  elif 20210619 > merge(user_month, user_day, user_year): 
    # Prints given date is too early
    print(merge(user_month, user_day, user_year), "is too early. No wordles occurred before 20210619. Enter a later date.")
  # If date too late
  else:
    # Prints given date is too recent
    print(merge(user_month, user_day, user_year), "is too recent. Our records only go as late as 20240421. Please enter an earlier date.")

# If user enters something other than 'w' or 'd'
else:
  # Error message
  print("Unrecognized option. Enter either 'w' or 'd'.")  
