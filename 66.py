#Create a function that takes a word from user and translates it using a dictionary of three words

d = dict( weather = "clima", earth = "terra", rain = "chuva" )

word = input("Enter word: ")
print(d[word])
