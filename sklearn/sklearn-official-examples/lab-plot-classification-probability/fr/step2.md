# Charger l'ensemble de données

Ensuite, nous chargeons l'ensemble de données iris à partir de Scikit-learn.

```python
iris = datasets.load_iris()
X = iris.data[:, 0:2]  # we only take the first two features for visualization
y = iris.target
n_features = X.shape[1]
```
