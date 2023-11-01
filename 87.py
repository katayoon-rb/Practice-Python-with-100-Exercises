#Add the missing items to the file

checklist = ["Portugal", "Germany", "Spain"]
checklist = [i + "\n" for i in checklist]

with open("87 countries_missing.txt", "r") as file:
    content = file.readlines()

updated_list = sorted(checklist + content)

with open("87 countries_missing_fixed.txt", "w") as file:
    for i in updated_list:
        file.write(i)
