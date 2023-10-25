#Create a function that takes a string and returns the number of words

def count(str):
    strList = str.split(" ")
    return len(strList)

print(count("Hey there it's me!"))
