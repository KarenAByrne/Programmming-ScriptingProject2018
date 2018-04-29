#Karen Byrne 02/04/2018
#Project due 29th April 2018

import numpy as np
import matplotlib.pyplot as pl
import pandas
import math

#with open("data/iris.csv") as data:

data = np.genfromtxt("data/iris.csv", delimiter = ',')

# Name the columns of data below

setosasepallength = data[:50,0]
setosasepalwidth = data[:50,1]
setosapetallength = data[:50,2]
setosapetalwidth = data[:50,3]

versicolorsepallength = data[50:99,0]
versicolorsepalwidth = data[50:99,1]
versicolorpetallength = data[50:99,2]
versicolorpetalwidth = data[50:99,3]

virginicasepallength = data[100:149,0]
virginicasepalwidth = data[100:149,1]
virginicapetallength = data[100:149,2]
virginicapetalwidth = data[100:149,3]

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


# calculate the max of each attribute for each species
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

# calculate the min of each attribute for each species
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


#pl.scatter(setosapetallength)
pl.show()
pl.plot(setosapetallength)
pl.show()
pl.hist(setosapetalwidth)
pl.show()
pl.plot(setosapetalwidth)
pl.show()

# http://scikit-learn.org/stable/auto_examples/datasets/plot_iris_dataset.html
#pl.http://scikit-learn.org/stable/auto_examples/datasets/plot_iris_dataset.htmlxlabel('Sepal length')
#pl.ylabel('Sepal width')



# print the mean of each column from above
print("The average setosa sepal length is:", meansetosasepallength) 
print("The average virginica sepal length is:", meanvirginicasepallength)
print("The average versicolor sepal length is:", meanversicolorsepallength)

print("The average setosa sepal width is:", meansetosasepalwidth) 
print("The average virginica sepal width is:", meanvirginicasepalwidth)
print("The average versicolor sepal width is:", meanversicolorsepalwidth)  

print("The average setosa petal length is:", meansetosapetallength) 
print("The average virginica petal length is:", meanvirginicapetallength) 
print("The average versicolor petal length is:", meanversicolorpetallength) 

print("The average setosa petal width is:", meansetosapetalwidth) 
print("The average virginica petal width is:", meanvirginicapetalwidth) 
print("The average versicolor petal width is:", meanversicolorpetalwidth) 

# print the max of each column from above
print("The max setosa sepal length is:", maxsetosasepallength) 
print("The max virginica sepal length is:", maxvirginicasepallength)
print("The max versicolor sepal length is:", maxversicolorsepallength)

print("The max setosa sepal width is:", maxsetosasepalwidth) 
print("The max virginica sepal width is:", maxvirginicasepalwidth)
print("The average versicolor sepal width is:", maxversicolorsepalwidth)  

print("The max setosa petal length is:", maxsetosapetallength) 
print("The max virginica petal length is:", maxvirginicapetallength) 
print("The max versicolor petal length is:", maxversicolorpetallength) 

print("The max setosa petal width is:", maxsetosapetalwidth) 
print("The max virginica petal width is:", maxvirginicapetalwidth) 
print("The max versicolor petal width is:", maxversicolorpetalwidth) 


# print the min of each column from above
print("The min setosa sepal length is:", minsetosasepallength) 
print("The min virginica sepal length is:", minvirginicasepallength)
print("The min versicolor sepal length is:", minversicolorsepallength)

print("The min setosa sepal width is:", minsetosasepalwidth) 
print("The min virginica sepal width is:", minvirginicasepalwidth)
print("The min versicolor sepal width is:", minversicolorsepalwidth)  

print("The min setosa petal length is:", minsetosapetallength) 
print("The min virginica petal length is:", minvirginicapetallength) 
print("The min versicolor petal length is:", minversicolorpetallength) 

print("The min setosa petal width is:", minsetosapetalwidth) 
print("The min virginica petal width is:", minvirginicapetalwidth) 
print("The min versicolor petal width is:", minversicolorpetalwidth) 
