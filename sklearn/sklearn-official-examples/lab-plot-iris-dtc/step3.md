# Display Decision Tree Structure

Next, we will display the structure of a single decision tree trained on all the features of the Iris dataset.

```python
from sklearn.tree import plot_tree

plt.figure()
clf = DecisionTreeClassifier().fit(iris.data, iris.target)
plot_tree(clf, filled=True)
plt.title("Decision tree trained on all the iris features")
plt.show()
```
