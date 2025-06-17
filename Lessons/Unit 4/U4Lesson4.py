# The code does not output anything

def triangle(ch, num):
    if num == 1: 
        print(ch) 
        return
    else:  
        print(ch * num)  
        triangle(ch, num - 1)

ch = "#"
n = 8
triangle(ch, n)
