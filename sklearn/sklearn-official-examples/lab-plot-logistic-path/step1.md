# Load the Iris dataset

We will load the Iris dataset from the scikit-learn library. The dataset contains four features: Sepal length, Sepal width, Petal length, and Petal width. We will use only the first two features for binary classification.

```python
from sklearn import datasets

iris = datasets.load_iris()
X = iris.data
y = iris.target

X = X[y != 2] # Use only first two features for binary classification
y = y[y != 2]

X /= X.max() # Normalize X to speed-up convergence
```
