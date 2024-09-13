import math
d = 5 
def odd(d):
    rows = math.ceil(d/2)
    for spaces in range(rows-1,-1,-1):
        star = d - (spaces * 2)
        print(" " * spaces + "*" * star)
    for spaces in range(1,rows):
        star = d - (spaces * 2)
        print(" " * spaces + "*" * star)
odd(25)