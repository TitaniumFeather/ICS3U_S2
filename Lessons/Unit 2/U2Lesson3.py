print("Factorial Calculator:")
limiter = int(input("Enter a value for the upper limit, n: "))
limit = 1
factorialValue = 1

while limit <= limiter:
  factorialValue = factorialValue*limit
  print("%d! factorial is %d" % (limit, factorialValue))
  limit+=1
