#Write a script that extracts letters from files if letters are contained in "python" and puts the letters in a list

from glob import iglob

letters = []
file_list = iglob("letters/*.txt")
check = "python"

for filename in file_list:
    with open(filename,"r") as file:
        letter = file.read().strip("\n")
        if letter in check:
            letters.append(letter)

print(letters)
