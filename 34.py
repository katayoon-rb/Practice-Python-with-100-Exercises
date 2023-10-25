#The script throws an error (when global c is not there). Fix it so that the script prints the value assigned to c inside the function

# def foo():
#     c = 1
#     return c

# foo()

# print(c)


# A: the c value is not global


def foo():
    global c
    c = 1
    return c

foo()

print(c)
