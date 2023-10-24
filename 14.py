#Write a script that remove duplicates from a list
a = ["1", 1, "1", 2]
b = []
for i in a:
    if i not in b:
        b.append(i)