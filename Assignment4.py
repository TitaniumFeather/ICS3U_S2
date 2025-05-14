f = open("wordle.dat")

arr = []
date_arr = []

line = f.readline()
while line != "":
    line = f.readline()
    arr.append(line.split(" "))



print(arr)
