# Modify
items = ["Apples", "Bananas", "Cherries", "Dosa"]
sizes = []
for i in range(len(items)): # Predict A: State the purpose,
                            # data types, and any output
    sizeI = len(items[i])
    sizes.append(sizeI)

for i in range(len(sizes)): # Predict B: State the output
    print(sizes[i], items[i], end=": ")
    if len(items[i]) == sizes[i]:
      print(True)
    else:
      print(False)
