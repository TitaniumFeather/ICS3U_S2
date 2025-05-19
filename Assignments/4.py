# Initialize a list to hold all lines of data read from the file
data_rows = []
# List to store all dates converted to numerical form
all_dates = []
# List to store all Wordle solution words
all_words = []
# List of month abbreviations to help convert month names to numbers
month_array = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

# Try to open and read the wordle.dat file
try:
  # Open the file for reading
  fh = open("wordle.dat", "r")
  # Flag to track end of file
  eof = False
  # Loop until end of file
  while not eof:
    # Read and strip whitespace from the line
    line = fh.readline().strip()
    # Set eof flag if line is empty
    eof = (line == "")
    # If the line is not empty, split and append to data_rows
    if not eof:
      data_rows.append(line.split(" "))
  # Close the file after reading
  fh.close()
# Handle file-related errors
except OSError as err:
  # Print OSError if occurs
  print("OSError:", err)
# Handle unexpected end of file
except EOFError as err2:
  # Print EOFError and close the file
  print("EOFError:", err2)
  fh.close()

# Function to convert month, day, year into numerical date format
def combine_date_parts(temp_month, temp_day, temp_year):
  # Convert year to integer
  temp_year = int(temp_year)
  # Convert month to corresponding number (Jan = 1, etc.)
  temp_month = (month_array.index(temp_month) + 1)
  # Convert day to integer
  temp_day = int(temp_day)
  # Return combined date as YYYYMMDD integer
  return (temp_year * 10000) + (temp_month * 100) + temp_day

# Counter to loop through data_rows to convert dates
i = 0
# Loop through each row in data_rows
while i < len(data_rows):
  # Convert date parts to numerical date
  numerical_date = combine_date_parts(data_rows[i][0], data_rows[i][1], data_rows[i][2])
  # Append converted date to all_dates list
  all_dates.append(numerical_date)
  # Increment counter
  i += 1
    
# Counter for looping through rows to extract words
m = 0
# Loop through each row to extract the word (4th element)
while m < len(data_rows):
  # Append word to all_words list
  all_words.append(data_rows[m][3])
  # Increment counter
  m += 1

# Function to find the date a word was used
def find_word_date(search_word):
  # Counter for search logic
  i = 0
  # Flag to track if word is found
  counter = 0
  # Loop through all words to find the input word
  while i < len(all_words):
    # If the word matches (case-insensitive)
    if all_words[i] == search_word.upper():
      # Set flag to found
      counter = 1
    # Increment counter
    i += 1
  # If word found, return corresponding date
  if counter == 1:
    return all_dates[all_words.index(search_word.upper())]
  # If word not found, return 0
  else:
    return 0

# Function to return the word used on a specific date
def get_word_by_date(month, day, year):
  # Convert date inputs into numerical format
  input_date = combine_date_parts(month, day, year)
  # Loop through all stored dates
  for date in all_dates:
    # If input date matches a stored date
    if date == input_date:
      # Return the word that matches the date's index
      return all_words[all_dates.index(input_date)]

# Print welcome message
print("Welcome to the Wordle Database!")
# Ask the user whether to search by word or date
choice = input("Enter w if you are looking for a word, "
               "or d for a word on a certain date: ")

# If user chose to search by word
if choice == "w":
  # Ask for the word to search
  w = input("What word are you looking for? ")
  # If word is found, print its corresponding date
  if find_word_date(w) > 0:
    print("The word", w.upper(), "was the solution to the puzzle on", find_word_date(w))
  # If word not found, notify the user
  else:
    print(w.upper(), "was not found in the database.")

# If user chose to search by date
elif choice == "d":
  # Ask for year input
  user_year = input("Enter the year: ")
  # Ask for 3-letter month abbreviation and capitalize it
  user_month = input("Enter the month (3-letter abbreviation, as in 'Jan' for 'January'): ").capitalize()
  # Ask for the day
  user_day = input("Enter the day: ")
  # Convert input date into numerical format
  formatted_date = combine_date_parts(user_month, user_day, user_year)
  # If date is within Wordle's available range
  if 20210619 <= formatted_date <= 20240421:
    print("The word entered on", formatted_date, "was", get_word_by_date(user_month, user_day, user_year))
  # If date is too early
  elif 20210619 > formatted_date:
    print(formatted_date, "is too early. No wordles occurred before 20210619. Enter a later date.")
  # If date is too recent
  else:
    print(formatted_date, "is too recent. Our records only go as late as 20240421. Please enter an earlier date.")
