def swap(B, p, q):
    temp = B[p]
    B[p] = B[q]
    B[q] = temp

def trim(word):
    return word.strip()

def iSort(A):
    for i in range(1, len(A)):  
        for j in range(0, i):  
            if A[i] < A[j]: 
                swap(A, i, j) 

def printIt(A):
    for i in range(0, len(A), 10):
        line = ""
        for word in A[i:i + 10]:
            line += word + " " 
        print(line)

filename = "words40.dat"
fh = open(filename, "r")

words = fh.readlines()
for i in range(len(words)):
    words[i] = trim(words[i])

iSort(words)
printIt(words)
def sort(C): # A very inefficient sorting method!
    for i in range(len(C)):
        for j in range(len(C)):
            if (C[i] < C[j]):
                swap(C, i, j)

A = [4, -1, 7, 3, 9, 0, 11, 2, 14]
sort(A)
print(A)
