"""
Author : Muhammed Adil
Student Number: 753209
Revision Date : 6/16/2025
Program : Credit Card Expiry and Validation Report
Description : Reads credit card data from a file, sorts by expiry date, validates card numbers using 
              the Luhn algorithm, and outputs status to both the screen and an output file.

VARIABLE DICTIONARY :
    arr (list) - Stores all lines read from the input file (excluding the header)
    FullName (list) - Stores full names (first and last) of all cardholders
    CCTypes (list) - Stores the type of each credit card (e.g., VISA, Mastercard)
    CCNumbers (list) - Stores the credit card numbers as strings
    Expiry_Dates (list) - Stores expiry dates in the format YYYYMM as integers
    f (file object) - File handle used to read from the input file
    line (str) - Temporarily stores each line read from the input file
    EndOfFile (bool) - Boolean flag to check for end-of-file during reading
    x (str) - Temporarily stores each credit card entry from the input list during processing
    GivenName (str) - First name of a cardholder (extracted from input line)
    Surname (str) - Last name of a cardholder (extracted from input line)
    CCType (str) - Type of the credit card (extracted from input line)
    CCNumber (str) - Credit card number (extracted from input line)
    Name (str) - Concatenated full name of the cardholder
    Expiry_Date (int) - Concatenated and converted YYYYMM expiry date
    validity (str) - Stores "VALID" or "INVALID" based on result of Luhn validation
"""

"""
Function to reverse a given string.
Parameters:
    string (str): Word to be reverse
    reversed_str (str): Reversed version of string
    i (int): Index used to iterate through string
"""
def reverse(string):
    # Initialize an empty string to hold the reversed result
    reversed_str = ""  
    # Iterate from end to start of string
    for i in range(len(string) - 1, -1, -1):
        # Append each character in reverse order
        reversed_str += string[i]  
    # Return the reversed string
    return reversed_str  

"""
Function to validate a card number using the Luhn algorithm.
Parameters:
    cardNumber (str): A string of digits representing the number to validate.
    total (int): Accumulates the total sum used to determine if the number is valid.
    digit (int): The numeric value of the current digit being processed.
    doubled (int): The result of doubling every second digit from the right (with adjustment if > 9).
    i (int): Index used for the for loop.
"""
def luhnCheck(cardNumber):
    # Reverse the card number using reverse()
    cardNumber = reverse(cardNumber)  
    # Initialize total sum for validation
    total = 0  
    for i in range(len(cardNumber)):
        # Convert character to integer
        digit = int(cardNumber[i])  
        # Double every second digit from the right
        if i % 2 == 1:  
            doubled = digit * 2
            # If result is double-digit:
            if doubled > 9:  
                # Subtract nine
                doubled -= 9
            # Add adjusted value
            total += doubled  
        else:
            # Add digit directly if not doubled
            total += digit  
    # Return True (valid), if total is divisible by 10. If not, False.
    return total % 10 == 0  

"""
Function to add zero in the date if month is single digit (like Jan = 1).
This makes it possible to sort.
Parameters:
    n (int): The 5 digit date (eg. 20231 for Jan 2023)
    n_str (str): String format of 5 digit date
"""
def insert_zero_at_index_4(n):
    # Convert number to string
    n_str = str(n)
    # Insert zero in required place (eg. 20231 becomes 202301 for Jan 2025)
    return int(n_str[:4] + "0" + n_str[4:])  

"""
Function to perform merge sort on multiple parallel arrays.
Parameters:
    arr (list): Primary array used for sorting
    arr2 (list): Parallel array to be reordered based on arr's sorting 
    arr3 (list): Parallel array to be reordered based on arr's sorting 
    arr4 (list): Parallel array to be reordered based on arr's sorting 
    l (int): Left index of the subarray to sort.
    r (int): Right index of the subarray to sort.
    m (int): Middle index used to divide the array into two halves for recursive sorting.
"""
def mergeSort(arr, arr2, arr3, arr4, l, r):
    if l < r:
        # Calculate the middle index
        m = l + (r - l) // 2
        # Recursively sort the first half
        mergeSort(arr, arr2, arr3, arr4, l, m)
        # Recursively sort the second half
        mergeSort(arr, arr2, arr3, arr4, m + 1, r)
        # Merge the two halves
        merge(arr, arr2, arr3, arr4, l, m, r)  

"""
Function to merge two sorted subarrays of multiple parallel arrays.
Parameters:
    arr (list): Primary array to be merged.
    arr2 (list): Parallel array corresponding to arr.
    arr3 (list): Parallel array corresponding to arr.
    arr4 (list): Parallel array corresponding to arr.
    l (int): Left index of the subarray.
    m (int): Middle index, dividing the two subarrays.
    r (int): Right index of the subarray.
    n1 (int): Number of elements in the left subarray.
    n2 (int): Number of elements in the right subarray.
    L, L2, L3, L4 (list): Temporary arrays holding the left halves of arr, arr2, arr3, arr4.
    R, R2, R3, R4 (list): Temporary arrays holding the right halves of arr, arr2, arr3, arr4.
    i (int): Index for traversing the left subarrays.
    j (int): Index for traversing the right subarrays.
    k (int): Index for placing merged elements back into the original arrays.
"""
def merge(arr, arr2, arr3, arr4, l, m, r):
    n1 = m - l + 1  # Size of left subarray
    n2 = r - m  # Size of right subarray

    # Create temp arrays for all input arrays
    L = [0] * n1
    L2 = [0] * n1
    L3 = [0] * n1
    L4 = [0] * n1
    R = [0] * n2
    R2 = [0] * n2
    R3 = [0] * n2
    R4 = [0] * n2

    # Copy data to temporary left arrays
    for i in range(n1):
        L[i] = arr[l + i]
        L2[i] = arr2[l + i]
        L3[i] = arr3[l + i]
        L4[i] = arr4[l + i]

    # Copy data to temporary right arrays
    for j in range(n2):
        R[j] = arr[m + 1 + j]
        R2[j] = arr2[m + 1 + j]
        R3[j] = arr3[m + 1 + j]
        R4[j] = arr4[m + 1 + j]

    # Merge the temp arrays back into the original arrays
    i = 0  # Initial index of left array
    j = 0  # Initial index of right array
    k = l  # Initial index of merged array

    while i < n1 and j < n2:
        if L[i] <= R[j]:  # Compare expiry date
            arr[k] = L[i]
            arr2[k] = L2[i]
            arr3[k] = L3[i]
            arr4[k] = L4[i]
            i += 1
        else:
            arr[k] = R[j]
            arr2[k] = R2[j]
            arr3[k] = R3[j]
            arr4[k] = R4[j]
            j += 1
        k += 1

    # Copy any remaining elements of left side
    while i < n1:
        arr[k] = L[i]
        arr2[k] = L2[i]
        arr3[k] = L3[i]
        arr4[k] = L4[i]
        i += 1
        k += 1

    # Copy any remaining elements of right side
    while j < n2:
        arr[k] = R[j]
        arr2[k] = R2[j]
        arr3[k] = R3[j]
        arr4[k] = R4[j]
        j += 1
        k += 1

# Will store lines of file as lists
arr = []  

try:
    # Open file for reading
    f = open("data.dat", "r")
    EndOfFile = False
    while not EndOfFile:
        # Read and clean line
        line = f.readline().strip()
        # End loop on empty line
        EndOfFile = (line == "")  
        if not EndOfFile:
            # Split line by comma and store in arr[]
            arr.append(line.split(","))  
    # Close the file after reading
    f.close()  
except OSError:
    # Handle file opening errors
    print("OSError")  
except EOFError:
    # Handle end-of-file errors
    print("EOFError")  

# Remove header row from data
arr.remove(arr[0])  

# Create separate lists for the data
FullName = []
CCTypes = []
CCNumbers = []
Expiry_Dates = []

# Process each entry in the 2d array
for x in range(len(arr)):
    # First name
    GivenName = arr[x][0]
    # Last name
    Surname = arr[x][1]  
    # Full name
    Name = GivenName + ' ' + Surname  
    # Credit card type
    CCType = arr[x][2]  
    # Credit card number
    CCNumber = arr[x][3]  
    # If expiry date is in the form YYYYM
    if len(arr[x][5] + arr[x][4]) == 5:  
        # Month might be single-digit (convert to int and add zero)
        Expiry_Date = int(insert_zero_at_index_4(arr[x][5] + arr[x][4]))
    # If expiry date is the form YYYYMM
    else:
        # Keep it same but convert to int (so it can be sorted)
        Expiry_Date = int(arr[x][5] + arr[x][4])
    # Append all data to respective lists
    FullName.append(Name) # NAME
    CCTypes.append(CCType) # CARD TYPE
    CCNumbers.append(CCNumber) # CARD NUMBER
    Expiry_Dates.append(Expiry_Date) # EXPIRY DATE FOR CARD

# Sort all lists by expiry date using merge sort
mergeSort(Expiry_Dates, FullName, CCNumbers, CCTypes, 0, len(Expiry_Dates) - 1)

# ANSI escape codes for terminal color formatting
RED = "\033[91m"      # Red color for expired cards
YELLOW = "\033[93m"   # Yellow color for soon-to-expire cards
GREEN = "\u001b[32m"  # Green color for valid cards
RESET = "\033[0m"     # Reset to default terminal color

# Print sorted and validated (Luhn checked) results
for i in range(len(Expiry_Dates)):
    # If valid (using Luhn check):
    if luhnCheck(CCNumbers[i]):
        validity = "VALID"
    # If not:
    else:
        validity = "INVALID"
    # Cards that are expired (not in May or June 2025)
    if Expiry_Dates[i] < 202505:
        # Print result in the designated format
        print(("%-37s %-15s %-20s %-10s %-25s %-5s") % (FullName[i] + ':', "\U0001F4B3" + " " + CCTypes[i], '#' + CCNumbers[i], Expiry_Dates[i], RED + "EXPIRED" + RESET, " | " + GREEN + validity + RESET))
    
    # Cards that expire in May or June 2025
    elif Expiry_Dates[i] == 202506 or Expiry_Dates[i] == 202505:
        print(("%-37s %-15s %-20s %-10s %-25s") % (FullName[i] + ':',"\U0001F4B3" + " " + CCTypes[i], '#' + CCNumbers[i], Expiry_Dates[i], YELLOW + "RENEW IMMEDIATELY" + RESET + " | " + GREEN + validity + RESET))
    
    else:
        # Skip cards after JUNE 2025
        continue  
