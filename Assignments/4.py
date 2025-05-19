data_rows = []
all_dates = []
all_words = []
month_array = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

try:
    fh = open("wordle.dat", "r")
    eof = False
    while not eof:
        line = fh.readline().strip()
        eof = (line == "")
        if not eof:
            data_rows.append(line.split(" "))
            last = len(data_rows) - 1  # Keeps track of the last index, if needed
    fh.close()
except OSError as err:
    print("OSError:", err)
except EOFError as err2:
    print("EOFError:", err2)
    fh.close()

def combine_date_parts(temp_month, temp_day, temp_year):
    temp_year = int(temp_year)
    temp_month = (month_list.index(temp_month) + 1)
    temp_day = int(temp_day)
    return (temp_year*1000) + (temp_month*100) + temp_day

row_index = 0
while row_index < len(data_rows):
    all_dates.append(combine_date_parts(data_rows[row_index][0], data_rows[row_index][1], data_rows[row_index][2]))


    all_words.append(data_rows[row_index][3])
    row_index += 1

def find_word_date(search_word):
    for temp_word in all_words:
        if temp_word == search_word.upper():
            return all_dates[all_words.index(search_word.upper())]
    return 0

def find_date_word(temp_month, temp_day, temp_year):
    formatted_date = combine_date_parts(temp_month, temp_day, temp_year)
    for search_date in all_dates:
        if search_date == formatted_date:
            return all_words[all_dates.index(formatted_date)]

print("Welcome to the Wordle Database!")
user_option = input("Enter w if you are looking for a word, "
                    "or d for a word on a certain date: ")

if user_option == "w":
    user_guess = input("What word are you looking for? ")
    if find_word_date(user_guess) > 0:
        print("The word", user_guess.upper(), "was the solution to the puzzle on", find_word_date(user_guess))
    else:
        print(user_guess.upper(), "was not found in the database.")
elif user_option == "d":
    input_year = input("Enter the year: ")
    input_month = input("Enter the month (3-letter abbreviation, as in 'Jan' for 'January'): ").capitalize()
    input_day = input("Enter the day: ")
    formatted_date = combine_date_parts(input_month, input_day, input_year)
    if 20210619 <= formatted_date <= 20240421:
        print("The word entered on", formatted_date, "was", find_date_word(input_month, input_day, input_year))
    elif 20210619 > formatted_date:
        print(formatted_date, "is too early. No Wordles occurred before 20210619. Enter a later date.")
    else:
        print(formatted_date, "is too recent. Our records only go as late as 20240421. Please enter an earlier date.")
