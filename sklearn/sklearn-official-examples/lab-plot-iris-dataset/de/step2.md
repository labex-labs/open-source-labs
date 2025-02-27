# Den Iris-Datensatz laden

Wir werden den Iris-Datensatz mit der in Scikit-learn integrierten Funktion `load_iris` laden.

```python
iris = datasets.load_iris()
X = iris.data[:, :2]  # wir nehmen nur die ersten zwei Features.
y = iris.target
```
