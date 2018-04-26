#Karen Byrne 02/04/2018
#Project due 29th April 2018

import numpy as np
import matplotlib.pyplot as pl
import pandas
import math

with open("data/iris.csv") as data:

    data = np.genfromtxt("data/iris.csv", delimiter = ',')

# Name the columns of data below

setosasepallength = data[:50,0]
setosasepalwidth = data[:50,1]
setosapetallength = data[:50,2]
setosapetalwidth = data[:50,3]

versicolorsepallength = data[50:50,0]
versicolorsepalwidth = data[50:50,1]
versicolorpetallength = data[50:50,2]
versicolorpetalwidth = data[50:50,3]

virginicasepallength = data[100:50,0]
virginicasepalwidth = data[100:50,1]
virginicapetallength = data[100:50,2]
virginicapetalwidth = data[100:50,3]

# calculate the mean of each measurement for each of the 3 species
meansetosasepallength = np.mean(setosasepallength)
meansetosasepalwidth = np.mean(setosasepalwidth)
meansetosapetallength = np.mean(setosapetallength)
meansetosapetalwidth = np.mean(setosapetalwidth)

meanversicolorsepallength = np.mean(versicolorsepallength)
meanversicolorsepalwidth = np.mean(versicolorsepalwidth)
meanversicolorpetallength = np.mean(versicolorpetallength)
meanversicolorpetalwidth = np.mean(versicolorpetalwidth)

meanvirginicasepallength = np.mean(virginicasepallength)
meanvirginicasepalwidth = np.mean(virginicasepalwidth)
meanvirginicapetallength = np.mean(virginicapetallength)
meanvirginicapetalwidth = np.mean(virginicapetalwidth)


# calculate the max of each column
maxsetosasepallength = np.max(setosasepallength)
maxsetosasepalwidth = np.max(setosasepalwidth)
maxsetosapetallength = np.max(setosapetallength)
maxsetosapetalwidth = np.max(setosapetalwidth)

maxversicolorsepallength = np.max(versicolorsepallength)
maxversicolorsepalwidth = np.max(versicolorsepalwidth)
maxversicolorpetallength = np.max(versicolorpetallength)
maxversicolorpetalwidth = np.max(versicolorpetalwidth)

maxvirginicasepallength = np.max(virginicasepallength)
maxvirginicasepalwidth = np.max(virginicasepalwidth)
maxvirginicapetallength = np.max(virginicapetallength)
maxvirginicapetalwidth = np.max(virginicapetalwidth)

# calcualte the min of each column
minsetosasepallength = np.min(setosasepallength)
minsetosasepalwidth = np.min(setosasepalwidth)
minsetosapetallength = np.min(setosapetallength)
minsetosapetalwidth = np.min(setosapetalwidth)

minversicolorsepallength = np.min(versicolorsepallength)
minversicolorsepalwidth = np.min(versicolorsepalwidth)
minversicolorpetallength = np.min(versicolorpetallength)
minversicolorpetalwidth = np.min(versicolorpetalwidth)

minvirginicasepallength = np.min(virginicasepallength)
minvirginicasepalwidth = np.min(virginicasepalwidth)
minvirginicapetallength = np.min(virginicapetallength)
minvirginicapetalwidth = np.min(virginicapetalwidth)


pl.scatter(setosapetallength)
pl.show()
pl.plot(setosapetallength)
pl.show()
pl.hist(setosapetalwidth)
pl.show()
pl.plot(setosapetalwidth)
pl.show()

# http://scikit-learn.org/stable/auto_examples/datasets/plot_iris_dataset.html
pl.xlabel('Sepal length')
pl.ylabel('Sepal width')



# print the mean of each column from above
print("The average setosa sepal length is:", meansetosasepallength) 
print("The average virginica sepal length is:", meanvirginicasepallength)
print("The average versicolor sepal length is:", meanversicolorsepallength)

print("The average setosa sepal length is:", meansetosasepallength) 
print("The average virginica sepal length is:", meanvirginicasepallength)
print("The average versicolor sepal length is:", meanversicolorsepallength)  

print("The average setosa petal length is:", meansetosapetallength) 
print("The average setosa petal width is:", meansetosapetalwidth) 
print("The average setosa sepal length is:", meansetosasepallength) 
print("The average setosa sepal width is:", meansetosasepalwidth) 

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
