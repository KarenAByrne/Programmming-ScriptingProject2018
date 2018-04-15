#Karen Byrne 02/04/2018
#Project due 29th April 2018

import numpy as np
import matplotlib.pyplot as pl
import math

print(math.factorial(10))

with open("data/iris.csv") as data:

    data = np.genfromtxt("data/iris.csv", delimiter = ',')

# Name the columns of data below
petallength = data[:,0]
meanpetallength = np.mean(data[:,0])
petalwidth = data[:,1]
meanpetalwidth = np.mean(data[:,1])
sepallength = data[:,2]
meansepallength = np.mean(data[:,2])
sepalwidth = data[:,3]
meansepalwidth = np.mean(data[:,3])

pl.hist(petallength)
pl.show()

#print the mean of each column from above
print("The average petal length is:", meanpetallength) 
print("The average petal width is:", meanpetalwidth) 
print("The average sepal length is:", meansepallength) 
print("The average sepal width is:", meansepalwidth) 

 
