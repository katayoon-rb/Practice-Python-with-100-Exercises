#Create a function like in the previous exercise, but taking into consideration that commas without space can separate words.
def count(filepath):
    with open(filepath, 'r') as file:
        str = file.read().replace(",", " ").split(" ")
        return len(str)

print(count("37 words2.txt"))