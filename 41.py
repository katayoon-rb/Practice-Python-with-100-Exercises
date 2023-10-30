#FromScratch - Create a script that generates a file where all letters of English alphabet are listed one in each line

import string

with open("letters.txt", "w") as file:
    for letter in string.ascii_lowercase:
        file.write(letter + "\n")
