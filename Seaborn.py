# Karen Byrne 29th April 2018
#https://stackoverflow.com/questions/45862223/use-different-colors-in-scatterplot-for-iris-dataset?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
# I found this code which returns a scatter plot showing the clusters in the data
#I could not get the file to run correctly in time for the deadline but it is somwthing to work from


import matplotlib.pyplot as plt
import seaborn as sns
iris = sns.load_dataset("data/iristest.csv")

ratio = iris["sepal_length"]/iris["sepal_width"]

for name, group in iris.groupby("species"):
    plt.scatter(group.index, ratio[group.index], label=name)

plt.legend()
plt.show()
