# Laden des Datensatzes

Der erste Schritt besteht darin, den Iris-Datensatz aus scikit-learn zu laden.

```python
from sklearn.datasets import load_iris

# Laden des Datensatzes
iris = load_iris()
X_iris = iris.data
y_iris = iris.target
```
