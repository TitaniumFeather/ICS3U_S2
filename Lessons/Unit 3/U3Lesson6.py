# Make:
def factorize(n):
  
  sum_num = 0
  arr = []
  
  for i in range(1, n):
    if n % i == 0:
      arr.append(i)
  
  return arr

# Make more
arr = factorize(n)

def total(arr):
  sum_num = 0
  for number in arr:
    sum_num += number
  
  return sum_num

print(total(arr))

# Optional "assignment form:
n = int(input("Please enter a number"))

def factorize(n):
  
  sum_num = 0
  arr = []
  
  for i in range(1, n):
    if n % i == 0:
      arr.append(i)
  
  for number in arr:
    sum_num += number
  
  print("Factor sum:", sum_num)
  
  if sum_num == n:
    print(n, "is perfect")
  elif sum_num < n:
    print(n, "is deficient")
  else:
    print(n, "is abundant")
    
print(factorize(n))
