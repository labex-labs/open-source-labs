# Load the Iris Dataset

We will load the Iris Dataset using the Scikit-learn built-in `load_iris` function.

```python
iris = datasets.load_iris()
X = iris.data[:, :2]  # we only take the first two features.
y = iris.target
```


