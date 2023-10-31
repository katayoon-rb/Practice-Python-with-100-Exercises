#Multiply the values of the text file in the URL by two and export the output to a new file

import pandas

data = pandas.read_csv("http://www.pythonhow.com/data/sampledata.txt")
data_2 = data * 2
data_2.to_csv("sampledata_x_2.txt", index=None)