n = int(input("Give me a value of n: "))
number = 0
factorialValue = 1
print("Counting from j = 1 to %d:" % n)
print("%0s %5s %11s" % ("j", "tri", "factorial"))

for i in range(n):
  number += (i+1)
  factorialValue = factorialValue*(i+1)
  print("%d %5d %11d" % (i+1, number, factorialValue))
