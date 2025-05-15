# Predict: Returns 7 in float form

# Modify 1:
def add(a: int, b: int) -> int:
  sum = a + b
  return sum

sum = add(7.0, 2.0)
print(sum) 


if isinstance(sum, float):
  print("True")
else:
  print("False")

# Modify 2:
def absd(n):
  if n < 0:
    return n * -1
  else:
    return n


print(absd(-435436456))

