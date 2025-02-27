# Daten laden

Der erste Schritt besteht darin, den Diabetes-Datensatz aus Scikit-Learn zu laden.

```python
from sklearn import datasets

X, y = datasets.load_diabetes(return_X_y=True)
```
