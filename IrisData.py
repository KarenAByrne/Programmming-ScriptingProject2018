#Karen Byrne 02/04/2018
#Project due 29th April 2018

import numpy as np
import matplotlib.pyplot as pl
import math

with open("data/iris.csv") as data:

    data = np.genfromtxt("data/iris.csv", delimiter = ',')

# Name the columns of data below
petallength = data[:,0]
petalwidth = data[:,1]
sepallength = data[:,2]
sepalwidth = data[:,3]


# calculate the mean of each column
meanpetallength = np.mean(data[:,0])
meanpetalwidth = np.mean(data[:,1])
meansepallength = np.mean(data[:,2])
meansepalwidth = np.mean(data[:,3])

# calculate the max of each column
maxpetallength = np.max(data[:,0])
maxpetalwidth = np.max(data[:,1])
maxsepallength = np.max(data[:,2])
maxsepalwidth = np.max(data[:,3])

# calcualte the min of each column
minpetallength = np.min(data[:,0])
minpetalwidth = np.min(data[:,1])
minsepallength = np.min(data[:,2])
minsepalwidth = np.min(data[:,3])

pl.hist(petallength)
pl.show()
pl.plot(petallength)
pl.show()
pl.hist(petalwidth)
pl.show()
pl.plot(petalwidth)
pl.show()

# http://scikit-learn.org/stable/auto_examples/datasets/plot_iris_dataset.html
pl.xlabel('Sepal length')
pl.ylabel('Sepal width')



# print the mean of each column from above
print("The average petal length is:", meanpetallength) 
print("The average petal width is:", meanpetalwidth) 
print("The average sepal length is:", meansepallength) 
print("The average sepal width is:", meansepalwidth) 

# print the max of each column from above
print("The max petal length is:", maxpetallength) 
print("The max petal width is:", maxpetalwidth) 
print("The max sepal length is:", maxsepallength) 
print("The max sepal width is:", maxsepalwidth) 

# print the min of each column from above
print("The min petal length is:", minpetallength) 
print("The min petal width is:", minpetalwidth) 
print("The min sepal length is:", minsepallength) 
print("The min sepal width is:", minsepalwidth)  

#print(f."The range of the petal lenth is {minpetallength},{maxpetallength}.".capitalize)
