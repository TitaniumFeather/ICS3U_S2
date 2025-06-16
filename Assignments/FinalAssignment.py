def reverse(string):
  reversed_str = ""
  for i in range(len(string) - 1, -1, -1):
    reversed_str += string[i]
  return reversed_str

def luhnCheck(cardNumber):
  cardNumber = reverse(cardNumber)
  total = 0
  for i in range(len(cardNumber)):
    digit = int(cardNumber[i])
    if i % 2 == 1:
      doubled = digit * 2
      if doubled > 9:
        doubled -= 9
      total += doubled
    else:
      total += digit
  return total % 10 == 0

def insert_zero_at_index_4(n):
    n_str = str(n)
    return int(n_str[:4] + "0" + n_str[4:])

def mergeSort(arr, arr2, arr3, arr4, l, r):
    if l < r:
        m = l + (r - l) // 2
        mergeSort(arr, arr2, arr3, arr4, l, m)
        mergeSort(arr, arr2, arr3, arr4, m + 1, r)
        merge(arr, arr2, arr3, arr4, l, m, r)

def merge(arr, arr2, arr3, arr4, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    L = [0] * (n1)
    L2 = [0] * (n1)
    L3 = [0] * (n1)
    L4 = [0] * (n1)
    R = [0] * (n2)
    R2 = [0] * (n2)
    R3 = [0] * (n2)
    R4 = [0] * (n2)
    for i in range(0, n1):
        L[i] = arr[l + i]
        L2[i] = arr2[l + i]
        L3[i] = arr3[l + i]
        L4[i] = arr4[l + i]
    for j in range(0, n2):
        R[j] = arr[m + 1 + j]
        R2[j] = arr2[m + 1 + j]
        R3[j] = arr3[m + 1 + j]
        R4[j] = arr4[m + 1 + j]
    i = 0
    j = 0
    k = l
    while i < n1 and j < n2:
        if L[i] <= R[j]:
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
    while i < n1:
        arr[k] = L[i]
        arr2[k] = L2[i]
        arr3[k] = L3[i]
        arr4[k] = L4[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = R[j]
        arr2[k] = R2[j]
        arr3[k] = R3[j]
        arr4[k] = R4[j]
        j += 1
        k += 1

arr = []

try:
    f = open("data.dat", "r")
    EndOfFile = False  
    while not EndOfFile:
        line = f.readline().strip()  
        EndOfFile = (line == "")  
        if not EndOfFile:
            arr.append(line.split(","))  
    f.close()
except OSError:
    print("OSError")  
except EOFError:
    print("EOFError")

arr.remove(arr[0])

FullName = []
CCTypes = []
CCNumbers = []
Expiry_Dates = []

for x in range(len(arr)):
  GivenName = arr[x][0]
  Surname = arr[x][1]
  Name = GivenName + ' ' + Surname
  CCType = arr[x][2]
  CCNumber =  arr[x][3]
  if len(arr[x][5] + arr[x][4]) == 5:
    Expiry_Date = int(insert_zero_at_index_4(arr[x][5] + arr[x][4]))
  else:
    Expiry_Date = int(arr[x][5] + arr[x][4])
  FullName.append(Name)
  CCTypes.append(CCType)
  CCNumbers.append(CCNumber)
  Expiry_Dates.append(Expiry_Date)

mergeSort(Expiry_Dates, FullName, CCNumbers, CCTypes, 0, len(Expiry_Dates) - 1)

# ANSI color codes 
RED = "\033[91m"      # Red text for expired cards
YELLOW = "\033[93m"   # Yellow text for soon-to-expire cards
GREEN = "\u001b[32m"  # Green for valid cards
RESET = "\033[0m"     # Reset text color to default

for i in range(len(Expiry_Dates)):
  if luhnCheck(CCNumbers[i]):
    validity = "VALID (LUHN CHECK VERIFIED)"
  else: 
    validity = "INVALID"
  if Expiry_Dates[i] < 202505:
    print(("%-37s %-15s %-20s %-10s %-25s %-5s") % (FullName[i] + ':', "\U0001F4B3" + " " + CCTypes[i], '#' + CCNumbers[i], Expiry_Dates[i], RED + "EXPIRED" + RESET, " | " + GREEN + validity + RESET))
  elif Expiry_Dates[i] == 202506 or Expiry_Dates[i] == 202505:
      print(("%-37s %-15s %-20s %-10s %-25s") % (FullName[i] + ':', "\U0001F4B3" + " " + CCTypes[i], '#' + CCNumbers[i], Expiry_Dates[i], YELLOW + "RENEW IMMEDIATELY" + RESET + " | " + GREEN + validity + RESET))
  else:
    continue
