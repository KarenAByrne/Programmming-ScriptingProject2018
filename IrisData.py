#Karen Byrne 15/04/2018
#Project due 29th April 2018

import numpy as np
import matplotlib.pyplot as pl
import math

print(math.factorial(10))

with open("data/iris.csv") as data:

    data = np.genfromtxt("data/iris.csv", delimiter = ',')

#pl.plot(range[149], data[:,0])
#pl.show()

petallength = data[:,0]
meanpetallength = np.mean(data[:,0])
petalwidth = data[:,1]
meanpetalwidth = np.mean(data[:,1])
sepallength = data[:,2]
meansepallength = np.mean(data[:,2])
sepalwidth = data[:,3]
meansepalwidth = np.mean(data[:,3])

np.histogram(data[:,0])

print("The average petal length is:", meanpetallength) 
print("The average petal width is:", meanpetalwidth) 
print("The average sepal length is:", meansepallength) 
print("The average sepal width is:", meansepalwidth) 
