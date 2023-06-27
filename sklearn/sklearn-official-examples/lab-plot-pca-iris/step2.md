# Load the dataset

Next, we will load the Iris dataset using scikit-learn's `load_iris()` function. We will then separate the features (X) and target (y) variables.

```python
iris = datasets.load_iris()
X = iris.data
y = iris.target
```
