#Karen Byrne 02/04/2018
#Project due 29th April 2018

import numpy

with open("data/iris.csv") as Data:
   for line in Data:
       line = line.replace(',',' ') #Replaces commas from the line with a space
       print(line[:11],line[12:16].strip()) #Prints the first 12 (0-11)  characters with a 
       #space instead of a comma, strips 16 characters from the 12th char onwards

data = numpy.genfromtxt("data/iris.csv", delimiter = ',')

firstcol = data[:,0]
meanfirstcol = numpy.mean(data[:,0])
print("Average is:", meanfirstcol)