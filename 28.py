#Why is the error and how to fix it?

# def foo(a, b):
#     print(a + b)

# x = foo(2, 3) * 10


#A: A TypeError means you are using the wrong type to make an operation. Change print(a+b) to return a+b

def foo(a, b):
    return a + b

x = foo(2, 3) * 10
