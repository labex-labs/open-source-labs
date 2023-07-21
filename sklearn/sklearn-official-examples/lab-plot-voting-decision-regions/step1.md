# Load the Data

We will load the iris dataset using Scikit-Learn's `datasets` module. We will only use two features: sepal length and petal length.

```python
from sklearn import datasets

iris = datasets.load_iris()
X = iris.data[:, [0, 2]]
y = iris.target
```
