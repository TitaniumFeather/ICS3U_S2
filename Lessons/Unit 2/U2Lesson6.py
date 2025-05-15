import math

print("   N|  SQR|  Cubes|Roots")
print(" ---+-----+-------+-----")
for n in range(10, 190, 15):
  x = round(math.sqrt(n), 2)
  y = n**2
  z = n**3
  
  print("%4d|%5d|%7d|%5.2f" % (n, y, z, x))
