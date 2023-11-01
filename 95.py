#Create a program that asks the user to input values separated by commas and those values will be stored in a separate line each in a text file

line = input("Enter values: ").split(",")

with open("95 user_data_commas.txt", "a+") as file:
    for i in line:
        file.write(i + "\n")

