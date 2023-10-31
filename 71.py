#Count how many a the text file has

import requests

count_a = requests.get("http://www.pythonhow.com/data/universe.txt").text.count("a")
print(count_a)
