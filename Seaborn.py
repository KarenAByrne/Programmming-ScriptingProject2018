import matplotlib.pyplot as plt
import seaborn as sns
iris = sns.load_dataset("data/iristest.csv")

ratio = iris["sepal_length"]/iris["sepal_width"]

for name, group in iris.groupby("species"):
    plt.scatter(group.index, ratio[group.index], label=name)

plt.legend()
plt.show()