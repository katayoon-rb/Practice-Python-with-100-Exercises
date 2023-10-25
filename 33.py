#What will the script output?
# A: When the print calls the function, that will assign the value of c witch is 2

c = 1
def foo():
    c = 2
    return c
c = 3

print(foo())
