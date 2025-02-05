# Load the Data

Next, we load the iris dataset from Scikit-learn and select only the first two features for visualization purposes.

```python
iris = datasets.load_iris()
X = iris.data[:, :2]
y = iris.target
```
