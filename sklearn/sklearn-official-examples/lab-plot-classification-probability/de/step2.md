# Lade den Datensatz

Als nächstes laden wir den Iris-Datensatz aus Scikit-learn.

```python
iris = datasets.load_iris()
X = iris.data[:, 0:2]  # wir nehmen nur die ersten beiden Merkmale für die Visualisierung
y = iris.target
n_features = X.shape[1]
```
