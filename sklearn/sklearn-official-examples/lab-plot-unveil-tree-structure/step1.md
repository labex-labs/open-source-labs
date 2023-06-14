# Train a Decision Tree Classifier

First, we need to fit a decision tree classifier using the `load_iris` dataset from scikit-learn. This dataset contains 3 classes of 50 instances each, where each class refers to a type of iris plant. We will split the dataset into training and test sets and fit a decision tree classifier with a maximum of 3 leaf nodes.

```python
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier

iris = load_iris()
X = iris.data
y = iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

clf = DecisionTreeClassifier(max_leaf_nodes=3, random_state=0)
clf.fit(X_train, y_train)
```


