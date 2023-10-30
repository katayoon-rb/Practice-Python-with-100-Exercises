#Get the file in the attachment and produce the printed output
import json
from pprint import pprint

with open("57 company1.json","r") as file:
    d = json.load(file)


pprint(d)
