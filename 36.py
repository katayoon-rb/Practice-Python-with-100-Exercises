#Create a function that takes a text file and returns the number of words
def count(filepath):
    with open(filepath, 'r') as file:
        str = file.read().split(" ")
        return len(str)

print(count("36 words1.txt"))
