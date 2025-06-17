# Function to reverse a given string
def reverse(string):
    reversed_str = ""  # Initialize an empty string to hold the reversed result
    for i in range(len(string) - 1, -1, -1):  # Iterate from end to start of string
        reversed_str += string[i]  # Append each character in reverse order
    return reversed_str  # Return the reversed string

# Function to check credit card number validity using the Luhn algorithm
def luhnCheck(cardNumber):
    cardNumber = reverse(cardNumber)  # Reverse the card number for processing
    total = 0  # Initialize total sum for validation
    for i in range(len(cardNumber)):
        digit = int(cardNumber[i])  # Convert character to integer
        if i % 2 == 1:  # Double every second digit from the right
            doubled = digit * 2
            if doubled > 9:  # If result is double-digit, subtract 9
                doubled -= 9
            total += doubled  # Add adjusted value
        else:
            total += digit  # Add digit directly if not doubled
    return total % 10 == 0  # Valid if total is divisible by 10

# Inserts a '0' at the 5th index in a number, used to format expiry dates properly
def insert_zero_at_index_4(n):
    n_str = str(n)  # Convert number to string
    return int(n_str[:4] + "0" + n_str[4:])  # Insert zero after 4 digits

# Recursive Merge Sort to sort Expiry Dates, while keeping FullName, CCNumbers, and CCTypes in sync
def mergeSort(arr, arr2, arr3, arr4, l, r):
    if l < r:
        m = l + (r - l) // 2  # Calculate the middle index
        mergeSort(arr, arr2, arr3, arr4, l, m)  # Sort the first half
        mergeSort(arr, arr2, arr3, arr4, m + 1, r)  # Sort the second half
        merge(arr, arr2, arr3, arr4, l, m, r)  # Merge the two halves

# Merge function used by mergeSort to combine two sorted halves
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
        if L[i] <= R[j]:  # Compare primary key (expiry date)
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

arr = []  # Will store lines of file as lists

try:
    f = open("data.dat", "r")  # Open file for reading
    EndOfFile = False
    while not EndOfFile:
        line = f.readline().strip()  # Read and clean line
        EndOfFile = (line == "")  # End loop on empty line
        if not EndOfFile:
            arr.append(line.split(","))  # Split line by comma and store
    f.close()  # Close the file after reading
except OSError:
    print("OSError")  # Handle file opening errors
except EOFError:
    print("EOFError")  # Handle end-of-file errors

arr.remove(arr[0])  # Remove header row from data

# Create separate lists for structured data
FullName = []
CCTypes = []
CCNumbers = []
Expiry_Dates = []

# Process each entry in the file
for x in range(len(arr)):
    GivenName = arr[x][0]  # First name
    Surname = arr[x][1]  # Last name
    Name = GivenName + ' ' + Surname  # Full name
    CCType = arr[x][2]  # Credit card type
    CCNumber = arr[x][3]  # Credit card number

    # Create expiry date in format YYYYMM
    if len(arr[x][5] + arr[x][4]) == 5:  # Month might be single-digit
        Expiry_Date = int(insert_zero_at_index_4(arr[x][5] + arr[x][4]))
    else:
        Expiry_Date = int(arr[x][5] + arr[x][4])

    # Append all parsed data to respective lists
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

# Print sorted and validated results
for i in range(len(Expiry_Dates)):
    if luhnCheck(CCNumbers[i]):  # Run Luhn check
        validity = "VALID (LUHN CHECK VERIFIED)"
    else:
        validity = "INVALID"

    # Cards that are expired (before May 2025)
    if Expiry_Dates[i] < 202505:
        print(("%-37s %-15s %-20s %-10s %-25s %-5s") % (
            FullName[i] + ':',
            "\U0001F4B3" + " " + CCTypes[i],
            '#' + CCNumbers[i],
            Expiry_Dates[i],
            RED + "EXPIRED" + RESET,
            " | " + GREEN + validity + RESET))

    # Cards that expire in May or June 2025
    elif Expiry_Dates[i] == 202506 or Expiry_Dates[i] == 202505:
        print(("%-37s %-15s %-20s %-10s %-25s") % (
            FullName[i] + ':',
            "\U0001F4B3" + " " + CCTypes[i],
            '#' + CCNumbers[i],
            Expiry_Dates[i],
            YELLOW + "RENEW IMMEDIATELY" + RESET + " | " + GREEN + validity + RESET))

    else:
        continue  # Skip cards after JUNE 2025
