#Why do you get an error and how would you fix it?

# def foo(a=2, b):
#     return a + b

# print(foo(3, 4))



# You shouldn't the default value first

def foo(b, a = 2):
    return a + b

print(foo(3, 4))
