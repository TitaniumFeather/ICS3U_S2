# Modify
ar2 = [[3, 4, 1, 2, 6],
       [9, 2, 3, 7, 5],
       [4, 2, 1, 0, 3]]
one = 0
empty = []

for j in range(3):
  for i in range(5):
    one = one + ar2[j][i]
  empty.append(one)
  one = 0

print(empty)
